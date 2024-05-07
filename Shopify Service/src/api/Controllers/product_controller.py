from src.api.Controllers.token_controller import get_token_from_db
from src.Interactor.Dto.product_dto import product_dto
from src.Interactor.Logger.custom_logger import app_logger
from src.Interactor.Exception.custom_exceptions import UnauthorizedApiException , StoreNotFoundException
import requests

SHOPIFY_API_VERSION = "2023-10"

def get_all_products(store_name):
    access_token = get_token_from_db(store_name)
    
        
    if not access_token:   
        app_logger.error(f'No access token found for store: {store_name}')
        raise StoreNotFoundException

    url = f"https://{store_name}.myshopify.com/admin/api/{SHOPIFY_API_VERSION}/products.json"
    headers = {
        'X-Shopify-Access-Token': access_token
    }
    
    app_logger.info(f'Sending request to Shopify API to get all products for store: {store_name}')
    response = requests.get(url, headers=headers)

    app_logger.info(f'Shopify API Response: {response.json()}')
    app_logger.info(f'Shopify API Response Status Code: {response.status_code}')

    if response.status_code == 200:
        shopify_products = [product_dto(product) for product in response.json().get('products', [])]
        app_logger.info(f'Retrieved {len(shopify_products)} products from Shopify API')
        return shopify_products
    elif response.status_code == 401:
        app_logger.error('Unauthorized API call. Invalid API key or access token.')
        raise UnauthorizedApiException
    
    app_logger.warning(f'Failed to retrieve products from Shopify API. Status Code: {response.status_code}')
    return []








def get_product_by_id(store_name, product_ids):
    access_token = get_token_from_db(store_name)

    if not access_token:   
        app_logger.error(f'No access token found for store: {store_name}')
        raise StoreNotFoundException


    products = []

    if len(product_ids) == 1:
        url = f"https://{store_name}.myshopify.com/admin/api/{SHOPIFY_API_VERSION}/products/{product_ids[0]}.json"
        headers = {
            'X-Shopify-Access-Token': access_token
        }
        app_logger.info(f'Sending request to Shopify API to get product with ID: {product_ids[0]} for store: {store_name}')
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            product_data = response.json().get('product', {})
            products.append(product_dto(product_data))
            app_logger.info(f'Retrieved product with ID {product_ids[0]} from Shopify API')
        elif response.status_code == 401:
            app_logger.error('Unauthorized API call. Invalid API key or access token.')
            raise UnauthorizedApiException
        else:
            app_logger.warning(f'Failed to retrieve product with ID {product_ids[0]} from Shopify API. Status Code: {response.status_code}')
    
    elif len(product_ids) > 1:
        ids = ','.join(product_ids)
        url = f"https://{store_name}.myshopify.com/admin/api/{SHOPIFY_API_VERSION}/products.json?ids={ids}"
        headers = {
            'X-Shopify-Access-Token': access_token
        }
        app_logger.info(f'Sending request to Shopify API to get products with IDs: {product_ids} for store: {store_name}')
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            product_data_list = response.json().get('products', [])
            products.extend([product_dto(product_data) for product_data in product_data_list])
            app_logger.info(f'Retrieved {len(products)} products from Shopify API')
        elif response.status_code == 401:
            app_logger.error('Unauthorized API call. Invalid API key or access token.')
            raise UnauthorizedApiException
        else:
            app_logger.warning(f'Failed to retrieve products with IDs {product_ids} from Shopify API. Status Code: {response.status_code}')

    return products
