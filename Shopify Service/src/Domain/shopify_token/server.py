import uuid
import os
import json
import logging

from flask import redirect, request, render_template
from flask import Blueprint, request


from src.Domain.shopify_token.shopify_client import ShopifyStoreClient
from src.Domain.shopify_token import helpers

from src.api.Controllers.configuration_controller import create_configuration
from src.api.Controllers.store_user_controller import create_store_user
from src.api.Controllers.uninstall_conteoller import create_uninstall

from src.Interactor.Logger.custom_logger import app_logger




from dotenv import load_dotenv

load_dotenv()
WEBHOOK_APP_UNINSTALL_URL = os.environ.get('WEBHOOK_APP_UNINSTALL_URL')
print('webhook', WEBHOOK_APP_UNINSTALL_URL)


shopify_token_bp = Blueprint('shopify_token', __name__)


ACCESS_TOKEN = None
NONCE = None
ACCESS_MODE = []  # Defaults to offline access mode if left blank or omitted. https://shopify.dev/apps/auth/oauth/access-modes
SCOPES = ['write_script_tags','read_products','write_products','read_orders','write_orders','write_content']  # https://shopify.dev/docs/admin-api/access-scopes


@shopify_token_bp.route('/app_launched', methods=['GET'])
@helpers.verify_web_call
def app_launched():
    shop = request.args.get('shop')
    global ACCESS_TOKEN, NONCE

    if ACCESS_TOKEN:
        return render_template('welcome.html', shop=shop , token = ACCESS_TOKEN)
    
    
    NONCE = uuid.uuid4().hex
    redirect_url = helpers.generate_install_redirect_url(shop=shop, scopes=SCOPES, nonce=NONCE, access_mode=ACCESS_MODE)
    return redirect(redirect_url, code=302)


@shopify_token_bp.route('/app_installed', methods=['GET'])
@helpers.verify_web_call
def app_installed():
    state = request.args.get('state')
    global NONCE, ACCESS_TOKEN

    # Shopify passes our NONCE, created in #app_launched, as the `state` parameter, we need to ensure it matches!
    if state != NONCE:
        return "Invalid `state` received", 400
    NONCE = None

    # Ok, NONCE matches, we can get rid of it now (a nonce, by definition, should only be used once)
    # Using the `code` received from Shopify we can now generate an access token that is specific to the specified `shop` with the
    #   ACCESS_MODE and SCOPES we asked for in #app_installed
    shop = request.args.get('shop')
    code = request.args.get('code')
    ACCESS_TOKEN = ShopifyStoreClient.authenticate(shop=shop, code=code)
    
    # Create a configuration for the store
    try:
        create_configuration(shop.removesuffix('.myshopify.com') , ACCESS_TOKEN)
        app_logger.info(f"Configuration created successfully")
    except:
        app_logger.error(f"Failed to create configuration")
        
    # Create a store user for the store
    try:
        create_store_user(shop.removesuffix('.myshopify.com') , ACCESS_TOKEN)
        app_logger.info(f"Store User created successfully")
    except:
        app_logger.error(f"Failed to create store user")
    

    # We have an access token! Now let's register a webhook so Shopify will notify us if/when the app gets uninstalled
    # NOTE This webhook will call the #app_uninstalled function defined below
    shopify_client = ShopifyStoreClient(shop=shop, access_token=ACCESS_TOKEN)
    shopify_client.create_webook(address=WEBHOOK_APP_UNINSTALL_URL, topic="app/uninstalled")

    redirect_url = helpers.generate_post_install_redirect_url(shop=shop)
    return redirect(redirect_url, code=302)


@shopify_token_bp.route('/app_uninstalled', methods=['POST'])
@helpers.verify_webhook_call
def app_uninstalled():
    # https://shopify.dev/docs/admin-api/rest/reference/events/webhook?api[version]=2020-04
    # Someone uninstalled your app, clean up anything you need to
    # NOTE the shop ACCESS_TOKEN is now void!
    global ACCESS_TOKEN
    ACCESS_TOKEN = None
    
    # Create an uninstall for the store
    try:
        create_uninstall(request.headers.get('X-Shopify-Shop-Domain'))
        app_logger.info(f"Uninstall created successfully")
    except:
        app_logger.error(f"Failed to create uninstall")

    webhook_topic = request.headers.get('X-Shopify-Topic')
    webhook_payload = request.get_json()
    logging.error(f"webhook call received {webhook_topic}:\n{json.dumps(webhook_payload, indent=4)}")

    return "OK"


@shopify_token_bp.route('/data_removal_request', methods=['POST'])
@helpers.verify_webhook_call
def data_removal_request():
    # https://shopify.dev/tutorials/add-gdpr-webhooks-to-your-app
    # Clear all personal information you may have stored about the specified shop
    return "OK"