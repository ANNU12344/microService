from src.Domain.Constant import constant
from src.api.Controllers.token_controller import get_token_from_db
from src.Interactor.Exception.custom_exceptions import TokenNotFoundException
from src.Interactor.Logger.custom_logger import app_logger
from requests_oauthlib import OAuth1Session
import requests
import os
TUMBLR_POST_URL=constant.TUMBLR_POST_URL
from dotenv import load_dotenv

def update_blog(blog_id,post_id):
    url=f"https://api.tumblr.com/v2/blog/{blog_id}/posts/{post_id}"
    load_dotenv()
    Consumer_key = os.environ.get('TUMBLR_Consumer_Key')
    Consumer_secret_key = os.environ.get('TUMBLR_Secret_Key')
    print(f"blog_id:{blog_id},Consumer_key:{Consumer_key},Consumer_secret_key:{Consumer_secret_key}")
    access_oauth_token,access_oauth_token_secret,verify_code = ""# I have to set like how to get the token from the database
    if not (access_oauth_token,access_oauth_token_secret,verify_code):
        app_logger.error(f'No access token found for given consumer_key and consumer_secret_key :{Consumer_key,Consumer_secret_key}')
        raise TokenNotFoundException
    
    app_logger.info(f'Sending request to Tumblr API to post the blog  with blog ID,title and content : {blog_id}')
    oauth = OAuth1Session(Consumer_key, client_secret=Consumer_secret_key,resource_owner_key=access_oauth_token, resource_owner_secret=access_oauth_token_secret,verifier=verify_code)
        
    response = oauth.post(TUMBLR_POST_URL=url)
    app_logger.info(f'Tumblr API Response: {response.json()}')
    app_logger.info(f'Tumblr API Response Status Code: {response.status_code}')
    
    if response.status_code == 200:
        app_logger.info(f'created the post on tumblr ')
        return response
    elif response.status_code == 401:
        app_logger.error('Unauthorized API call. Invalid API key or access token.')