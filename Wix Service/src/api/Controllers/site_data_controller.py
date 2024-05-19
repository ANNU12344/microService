from src.api.Controllers.token_controller import get_token_from_db
from src.Interactor.Exception.custom_exceptions import UnauthorizedApiException , TokenNotFoundException
from src.Interactor.Logger.custom_logger import app_logger
# from src.Interactor.Dto.shop_dto import shop_dto
import requests

def get_site_data(wix_site, token = None):
    if token is None:
        access_token = get_token_from_db(wix_site)
    else:
        access_token = token
    
    if not access_token:
        app_logger.error(f'No access token found for wix site: {wix_site}')
        raise TokenNotFoundException
    url = f"https://www.wixapis.com/site-properties/v4/properties"
    headers = {
        'Authorization': access_token
        }
    app_logger.info(f'Sending request to Wix API to get info for wix site: {wix_site}')
    response = requests.get(url, headers=headers)
    
    app_logger.info(f'Shopify API Response: {response.json()}')
    app_logger.info(f'Shopify API Response Status Code: {response.status_code}')
    
    if response.status_code == 200:
        # site_object = shop_dto(response.json().get('properties', []))   
        app_logger.info(f'Retrieved wix site info from Wix API')
        return response.json()


    elif response.status_code == 401:
        app_logger.error('Unauthorized API call. Invalid API key or access token.')
        raise UnauthorizedApiException
    app_logger.warning(f'Failed to retrieve site info from Wix. Status Code: {response.status_code}')
    return response