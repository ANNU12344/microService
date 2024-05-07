from src.api.Controllers.token_controller import get_token_from_db
from src.Domain.Mapper.shopifyorder_mapper import map_json_to_shop
from src.Interactor.Dto.order_dto import order_dto
from src.Interactor.Exception.custom_exceptions import UnauthorizedApiException , StoreNotFoundException
from src.Interactor.Logger.custom_logger import app_logger
import requests

def get_all_orders(store_name):
    access_token = get_token_from_db(store_name)
    
    if not access_token:   
        app_logger.error(f'No access token found for store: {store_name}')
        raise StoreNotFoundException


    url = f"https://{store_name}.myshopify.com/admin/api/2023-10/orders.json?status=any"
    headers = {
        'X-Shopify-Access-Token': access_token
    }
    app_logger.info(f'Sending request to Shopify API to get all orders for store: {store_name}')
    response = requests.get(url, headers=headers)
    
    app_logger.info(f'Shopify API Response: {response.json()}')
    app_logger.info(f'Shopify API Response Status Code: {response.status_code}')
    
    if response.status_code == 200:
        shopify_orders = []
        for orders in response.json().get('orders', []):
            shopify_orders.append(order_dto(orders))
        app_logger.info(f'Retrieved {len(shopify_orders)} orders from Shopify API')
        return shopify_orders
    elif response.status_code == 401:
        app_logger.error('Unauthorized API call. Invalid API key or access token.')
        raise UnauthorizedApiException
    app_logger.warning(f'Failed to retrieve products from Shopify API. Status Code: {response.status_code}')
    return []

def get_order_by_id(store_name, order_ids):
    access_token = get_token_from_db(store_name)
    
    if not access_token:
        app_logger.error(f'No access token found for store: {store_name}')
        raise StoreNotFoundException
    

    orders = []
    for order_id in order_ids:
        url = f"https://{store_name}.myshopify.com/admin/api/2023-10/orders/{order_id}.json"
        headers = {
            'X-Shopify-Access-Token': access_token
        }
        response = requests.get(url, headers=headers)

        app_logger.info(f'Shopify API Response: {response.json()}')
        app_logger.info(f'Shopify API Response Status Code: {response.status_code}')
        

        if response.status_code == 200:
            order_data = response.json().get('order', {})
            orders.append(order_dto(response))
            app_logger.info(f'Retrieved order with ID {order_id} from Shopify API')
        elif response.status_code == 401:
            app_logger.error('Unauthorized API call. Invalid API key or access token.')
            raise UnauthorizedApiException
    return orders
