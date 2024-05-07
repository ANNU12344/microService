from src.api.Controllers.token_controller import get_token_from_db
from src.api.Controllers.collect_controller import get_all_collects
from src.Interactor.Logger.custom_logger import app_logger
from src.Interactor.Exception.custom_exceptions import UnauthorizedApiException , StoreNotFoundException
from src.Interactor.Dto.collection_dto import collection_dto

import requests


SHOPIFY_API_VERSION = "2023-07"


def get_all_collection(store_name):
    access_token = get_token_from_db(store_name)
    
        
    if not access_token:   
        app_logger.error(f'No access token found for store: {store_name}')
        raise StoreNotFoundException

    url = f"https://{store_name}.myshopify.com/admin/api/{SHOPIFY_API_VERSION}/custom_collections.json"
    headers = {
        'X-Shopify-Access-Token': access_token
    }
    
    app_logger.info(f'Sending request to Shopify API to get all collections for store: {store_name}')
    response = requests.get(url, headers=headers)

    app_logger.info(f'Shopify API Response: {response.json()}')
    app_logger.info(f'Shopify API Response Status Code: {response.status_code}')

    if response.status_code == 200:
        shopify_collections = [collection_dto(collection) for collection in response.json().get('custom_collections', [])]
        app_logger.info(f'Retrieved {len(shopify_collections)} collections from Shopify API')
        return shopify_collections
    elif response.status_code == 401:
        app_logger.error('Unauthorized API call. Invalid API key or access token.')
        raise UnauthorizedApiException
    
    app_logger.warning(f'Failed to retrieve collections from Shopify API. Status Code: {response.status_code}')
    return []









def get_collection_by_id(store_name, collection_ids):
    access_token = get_token_from_db(store_name)

    if not access_token:   
        app_logger.error(f'No access token found for store: {store_name}')
        raise StoreNotFoundException

    collections = []

    if len(collection_ids) == 1:
        url = f"https://{store_name}.myshopify.com/admin/api/{SHOPIFY_API_VERSION}/custom_collections/{collection_ids[0]}.json"
        headers = {
            'X-Shopify-Access-Token': access_token
        }
        app_logger.info(f'Sending request to Shopify API to get collection with ID: {collection_ids[0]} for store: {store_name}')
        response = requests.get(url, headers=headers)
        

        print(response.json())
        

        if response.status_code == 200:
            collection_data = response.json().get('custom_collection', {})
            collections.append(collection_dto(collection_data))
            app_logger.info(f'Retrieved collection with ID {collection_ids[0]} from Shopify API')
        elif response.status_code == 401:
            app_logger.error('Unauthorized API call. Invalid API key or access token.')
            raise UnauthorizedApiException
        else:
            app_logger.warning(f'Failed to retrieve collection with ID {collection_ids[0]} from Shopify API. Status Code: {response.status_code}')
    
    elif len(collection_ids) > 1:
        ids = ','.join(collection_ids)
        url = f"https://{store_name}.myshopify.com/admin/api/{SHOPIFY_API_VERSION}/custom_collections.json?ids={ids}"
        headers = {
            'X-Shopify-Access-Token': access_token
        }
        app_logger.info(f'Sending request to Shopify API to get collections with IDs: {collection_ids} for store: {store_name}')
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            collection_data_list = response.json().get('custom_collections', [])
            collections.extend([collection_dto(collection_data) for collection_data in collection_data_list])
            app_logger.info(f'Retrieved {len(collections)} collections from Shopify API')
        elif response.status_code == 401:
            app_logger.error('Unauthorized API call. Invalid API key or access token.')
            raise UnauthorizedApiException
        else:
            app_logger.warning(f'Failed to retrieve collections with IDs {collection_ids} from Shopify API. Status Code: {response.status_code}')

    return collections
