from src.api.Controllers.token_controller import get_token_from_db
from src.Interactor.Dto.post_dto import post_dto
from src.Interactor.Logger.custom_logger import app_logger
from src.Interactor.Exception.custom_exceptions import UnauthorizedApiException , SiteNotFoundException
import requests

def get_all_post(wix_site):
    access_token = get_token_from_db(wix_site)
      
    if not access_token:   
        app_logger.error(f'No access token found for store: {wix_site}')
        raise SiteNotFoundException

    url = f"https://www.wixapis.com/v3/posts"
    headers = {
        'Authorization': access_token
        }
    
    app_logger.info(f'Sending request to Wix API to get all posts for wix site: {wix_site}')
    response = requests.get(url, headers=headers)
    app_logger.info(f'Wix API Response Status Code: {response.status_code}')
    app_logger.info(f'Wix API Response: {response.json()}')
   

    if response.status_code == 200:
        wix_post = [post_dto(post) for post in response.json().get('posts', [])]
        app_logger.info(f'Retrieved {len(wix_post)} products from wix API')
        return  wix_post
    elif response.status_code == 401:
        app_logger.error('Unauthorized API call. Invalid API key or access token.')
        raise UnauthorizedApiException
    
    app_logger.warning(f'Failed to retrieve post from Wix API. Status Code: {response.status_code}')
    return []





def get_post_by_id(wix_site, post_ids):
    access_token = get_token_from_db(wix_site)
    if not access_token:   
        app_logger.error(f'No access token found for wix site: {wix_site}')
        raise SiteNotFoundException

    
    url = f"https://www.wixapis.com/v3/posts/{post_ids}"
    headers = {
        'Authorization': access_token
        }
    posts=[]
    app_logger.info(f'Sending request to Wix API to get post with ID: {post_ids} for store: {wix_site}')
    response = requests.get(url, headers=headers)
    app_logger.info(f'Wix API Response Status Code: {response.status_code}')

    if response.status_code == 200:
        post_data = response.json().get('post', {})
        posts.append(post_dto(post_data))
    elif response.status_code == 401:
        app_logger.error('Unauthorized API call. Invalid API key or access token.')
        raise UnauthorizedApiException
    else:
        app_logger.warning(f'Failed to retrieve post with ID {post_ids[0]} from Wix API. Status Code: {response.status_code}')
    
    return posts