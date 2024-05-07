
# from builtins import input
# from flask import Blueprint
# from src.Domain.Constant import constant
# import code
# from requests_oauthlib import OAuth1Session
# tumblr_token_bp = Blueprint('shopify_token', __name__)

# consumer_key=constant.TUMBLR_Consumer_Key
# consumer_secret=constant.TUMBLR_Secret_Key
# request_token_url = constant.TUMBLR_REQUEST_TOKEN_URL
# authorize_url = constant.TUMBLR_Authorize
# access_token_url = constant.TUMBLR_ACCESS_TOKEN_URL


# def new_oauth(consumer_key,consumer_secret):
#     print('Retrieve consumer key and consumer secret')
#     # STEP 1: Obtain request token
#     oauth_session = OAuth1Session(consumer_key, client_secret=consumer_secret)
#     fetch_response = oauth_session.fetch_request_token(request_token_url)
#     resource_owner_key = fetch_response.get('oauth_token')
#     resource_owner_secret = fetch_response.get('oauth_token_secret')

#     # STEP 2: Authorize URL + Response
#     full_authorize_url = oauth_session.authorization_url(authorize_url)

#     # Redirect to authentication page
#     print('\nPlease go here and authorize:\n{}'.format(full_authorize_url))
#     redirect_response = input('Allow then paste the full redirect URL here:\n').strip()

#     # Retrieve oauth verifier
#     oauth_response = oauth_session.parse_authorization_response(redirect_response)

#     verifier = oauth_response.get('oauth_verifier')

#     # STEP 3: Request final access token
#     oauth_session = OAuth1Session(
#         consumer_key,
#         client_secret=consumer_secret,
#         resource_owner_key=resource_owner_key,
#         resource_owner_secret=resource_owner_secret,
#         verifier=verifier
#     )
#     oauth_tokens = oauth_session.fetch_access_token(access_token_url)

#     tokens = {
#         'consumer_key': consumer_key,
#         'consumer_secret': consumer_secret,
#         'oauth_token': oauth_tokens.get('oauth_token'),
#         'oauth_token_secret': oauth_tokens.get('oauth_token_secret')
#     }

#     return tokens


       

# import os
# import json
# from typing import List
# import logging
# from flask import jsonify
# import requests
# from requests.exceptions import HTTPError

# from dotenv import load_dotenv

# load_dotenv()

# WIX_APP_ID = os.environ.get('APP_ID')
# WIX_SECRET_KEY = os.environ.get('App_SECRET_KEY')
# class TumblrClientToken():

#     def __init__(self,access_token: str):
#         self.access_token = access_token

#     @staticmethod
#     def authenticate(code: str) -> str:
#         url = f"https://www.wix.com/oauth/access"
#         payload = {
#             "client_id": WIX_APP_ID,
#             "client_secret": WIX_SECRET_KEY,
#             "grant_type": "authorization_code",
#             "code": code
#         }
#         try:
#             response = requests.post(url, json=payload)
#             response.raise_for_status()
#             return response.json()['access_token']
#         except HTTPError as ex:
#             logging.exception(ex)
#             return None