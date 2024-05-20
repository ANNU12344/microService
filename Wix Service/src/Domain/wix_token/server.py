import os
from src.Domain.wix_token import helpers
from flask import redirect, request, Blueprint
from src.Interactor.Logger.custom_logger import app_logger
from src.api.Controllers.configuration_controller import create_configuration
from src.api.Controllers.site_user_controller import create_site_user
from src.Domain.wix_token.wix_client import WixClientToken
from dotenv import load_dotenv

# from src.Infra.Repositories.token_repository import TokenRepository

load_dotenv()
INSTALL_FROM_LINK = os.environ.get('INSTALL_APP_USING_LINK')
wix_token_bp = Blueprint('wix_token', __name__)

@wix_token_bp.route('/app_launched', methods=['GET'])
def app_launched():
    token = request.args.get('token')
    redirect_url = helpers.generate_install_redirect_url(token)
    return redirect(redirect_url, code=302)


@wix_token_bp.route('/app_install', methods=['GET'])
def app_installed():
    code = request.args.get('code')
    wix_site=request.args.get('wix_site')
    access_token,refresh_token= WixClientToken.authenticate(code=code)
    
    # new_token=TokenRepository.create_token(wix_site,access_token,refresh_token)
    # try:
    #     app_logger.info(f'Creating configuration')
    #     create_configuration(wix_site, access_token)
    #     app_logger.info(f"Configuration created successfully")
    # except:
    #     app_logger.error(f"Failed to create configuration")

    # try:
    #     create_site_user(wix_site,access_token)
    #     app_logger.info(f"Store User created successfully")
    # except:
    #     app_logger.error(f"Failed to create store user")
    return access_token
    

@wix_token_bp.route('/refresh_token', methods=['GET'])
def refresh_token():
    refresh_token = request.args.get('refresh_token')
    ACCESS_TOKEN = WixClientToken.refresh(refresh=refresh_token)
    return ACCESS_TOKEN
