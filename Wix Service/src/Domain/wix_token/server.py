import os
from src.Domain.wix_token import helpers
from flask import redirect, request, Blueprint
from src.Infra.Repositories.token_repository import TokenRepository
from dotenv import load_dotenv
from src.Domain.wix_token.wix_client import WixClientToken

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
    print("Request received to get the access token")
    code = request.args.get('code')
    wix_site=request.args.get('wix_site')
    access_token,refresh_token= WixClientToken.authenticate(code=code)
    new_token=TokenRepository.create_token(wix_site,access_token,refresh_token)
    return access_token
    

@wix_token_bp.route('/refresh_token', methods=['GET'])
def refresh_token():
    refresh_token = request.args.get('refresh_token')
    ACCESS_TOKEN = WixClientToken.refresh(refresh=refresh_token)
    return ACCESS_TOKEN
