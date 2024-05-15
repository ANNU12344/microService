from src.api.Controllers.token_controller import get_token_from_db
from src.Interactor.Logger.custom_logger import app_logger
from src.Interactor.Exception.custom_exceptions import UnauthorizedApiException , TokenNotFoundException
import requests

def get_all_post(wix_site):
    access_token = get_token_from_db(wix_site)
    
        
    if not access_token:   
        app_logger.error(f'No access token found for store: {wix_site}')
        raise TokenNotFoundException

    url = f"https://www.wixapis.com/v3/posts"
    headers = {
        'Authorization': access_token
        }
    
    app_logger.info(f'Sending request to Wix API to get all post for wix site: {wix_site}')
    response = requests.get(url, headers=headers)
    app_logger.info(f'Wix API Response Status Code: {response.status_code}')
    app_logger.info(f'Wix API Response: {response.json()}')
   

    if response.status_code == 200:
        post_data = response.json()
        return post_data
    elif response.status_code == 401:
        app_logger.error('Unauthorized API call. Invalid API key or access token.')
        raise UnauthorizedApiException
    
    app_logger.warning(f'Failed to retrieve post from Shopify API. Status Code: {response.status_code}')
    return []





def get_post_by_id(wix_site, post_ids):
    access_token = get_token_from_db(wix_site)

    if not access_token:   
        app_logger.error(f'No access token found for wix site: {wix_site}')
        raise TokenNotFoundException

    
    url = f"https://www.wixapis.com/v3/posts/{post_ids}"
    headers = {
        'Authorization': access_token
        }
    
    app_logger.info(f'Sending request to Wix API to get post with ID: {post_ids} for store: {wix_site}')
    response = requests.get(url, headers=headers)
    app_logger.info(f'Wix API Response Status Code: {response.status_code}')

    if response.status_code == 200:
        app_logger.info(f'Retrieved post with ID {post_ids} from wix API')
        post_data = response.json()
        return post_data
    elif response.status_code == 401:
        app_logger.error('Unauthorized API call. Invalid API key or access token.')
        raise UnauthorizedApiException
    else:
        app_logger.warning(f'Failed to retrieve post with ID {post_ids[0]} from Wix API. Status Code: {response.status_code}')
    
    return response