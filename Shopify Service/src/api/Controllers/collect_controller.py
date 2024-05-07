from src.api.Controllers.token_controller import get_token_from_db
from src.Interactor.Dto.collect_dto import collect_dto
from src.Interactor.Logger.custom_logger import app_logger
from src.Interactor.Exception.custom_exceptions import UnauthorizedApiException , StoreNotFoundException
import requests

SHOPIFY_API_VERSION = "2023-04"

def get_all_collects(store_name):
    access_token = get_token_from_db(store_name)
    
    
    if not access_token:   
        app_logger.error(f'No access token found for store: {store_name}')
        raise StoreNotFoundException

    url = f"https://{store_name}.myshopify.com/admin/api/{SHOPIFY_API_VERSION}/collects.json"
    headers = {
        'X-Shopify-Access-Token': access_token
    }
    
    app_logger.info(f'Sending request to Shopify API to get all collects for store: {store_name}')
    response = requests.get(url, headers=headers)

    app_logger.info(f'Shopify API Response: {response.json()}')
    app_logger.info(f'Shopify API Response Status Code: {response.status_code}')

    if response.status_code == 200:
        shopify_collects = [collect_dto(collect) for collect in response.json().get('collects', [])]
        app_logger.info(f'Retrieved {len(shopify_collects)} collects from Shopify API')
        return shopify_collects
    elif response.status_code == 401:
        app_logger.error('Unauthorized API call. Invalid API key or access token.')
        raise UnauthorizedApiException
    
    app_logger.warning(f'Failed to retrieve collects from Shopify API. Status Code: {response.status_code}')
    return []