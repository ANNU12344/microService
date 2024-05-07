import requests
import json
from src.api.Controllers.token_controller import get_token_from_db
from src.Interactor.Exception.custom_exceptions import UnauthorizedApiException , StoreNotFoundException
from src.Interactor.Logger.custom_logger import app_logger


def update_collections(store, collection_id, title, description):
    access_token = get_token_from_db(store)
    
    if not access_token:
        app_logger.error(f'No access token found for store: {store}')
        raise StoreNotFoundException
    
    url = f'https://{store}.myshopify.com/admin/api/2024-01/custom_collections/{collection_id}.json'

    headers = {
        'Content-Type': 'application/json',
        'X-Shopify-Access-Token': access_token,
    }
    
    data = {
        "custom_collection": {
            "id": collection_id,
            "body_html": description,
            "title": title
        }
    }
    
    app_logger.info(f'Sending request to Shopify API to update collection with ID: {collection_id} for store: {store}')
    
    response = requests.put(url, data=json.dumps(data), headers=headers)
    
    app_logger.info(f'Request body: {json.dumps(data)}')
    
    app_logger.info(f'Shopify API Response: {response.json()}')
    app_logger.info(f'Shopify API Response Status Code: {response.status_code}')
    
    if response.status_code == 200:
        app_logger.info(f'Updated collection with ID {collection_id} from Shopify API')
        print(response.json())
        return True

    if response.status_code == 404:
        app_logger.warning(f'Failed to update collection from Shopify API. Status Code: {response.status_code} ,  Response: {response.text}')
        print(f'Error updating collection. Status code: {response.status_code}, Response: {response.text}')
        return False
    
    else:
        app_logger.warning(f'Failed to update collection from Shopify API. Status Code: {response.status_code} ,  Response: {response.text}')
        print(f'Error updating collection. Status code: {response.status_code}, Response: {response.text}')
        return False    
    

