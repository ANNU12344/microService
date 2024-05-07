# import os
# from flask import redirect, request, Blueprint
# from dotenv import load_dotenv
# from src.Domain.wix_token.tumblr_client import TumblrClientToken

# load_dotenv()
# INSTALL_FROM_LINK = os.environ.get('INSTALL_APP_USING_LINK')

# wix_token_bp = Blueprint('wix_token', __name__)


# @wix_token_bp.route('/app_launched', methods=['GET'])
# def app_launched():
#     return redirect(INSTALL_FROM_LINK)


# @wix_token_bp.route('/oauth_callback')
# def get_token():
#     token = request.args.get('token')
#     return token


# @wix_token_bp.route('/app_install', methods=['GET'])
# def app_installed():
#     print("Request recieved")
#     code = request.args.get('code')
#     ACCESS_TOKEN = WixClientToken.authenticate(code=code)
#     return ACCESS_TOKEN
