from src.api.Controllers.token_controller import get_token_from_db
from src.Interactor.Dto.shop_dto import shop_dto
from src.Interactor.Exception.custom_exceptions import UnauthorizedApiException , StoreNotFoundException
from src.Interactor.Logger.custom_logger import app_logger
import requests

def get_shop_data(store_name, token = None):
    if token is None:
        access_token = get_token_from_db(store_name)
    else:
        access_token = token
    
    if not access_token:
        app_logger.error(f'No access token found for store: {store_name}')
        raise StoreNotFoundException
    url = f"https://{store_name}.myshopify.com/admin/api/2023-10/shop.json"
    headers = {
        'X-Shopify-Access-Token': access_token
    }
    app_logger.info(f'Sending request to Shopify API to get info for store: {store_name}')
    response = requests.get(url, headers=headers)
    
    app_logger.info(f'Shopify API Response: {response.json()}')
    app_logger.info(f'Shopify API Response Status Code: {response.status_code}')
    
    if response.status_code == 200:
        shop_object = shop_dto(response.json().get('shop', []))   
        app_logger.info(f'Retrieved shop info from Shopify API')
        return shop_object
    elif response.status_code == 401:
        app_logger.error('Unauthorized API call. Invalid API key or access token.')
        raise UnauthorizedApiException
    app_logger.warning(f'Failed to retrieve shop info from Shopify API. Status Code: {response.status_code}')
    return []
