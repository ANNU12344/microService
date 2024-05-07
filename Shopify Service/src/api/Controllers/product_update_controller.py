import requests
import json
from src.api.Controllers.token_controller import get_token_from_db
from src.Interactor.Exception.custom_exceptions import UnauthorizedApiException , StoreNotFoundException
from src.Interactor.Logger.custom_logger import app_logger


def update_products(store, product_id, title, description):
    print(f"store: {store}, product_id: {product_id}, title: {title}, description: {description}")
    access_token = get_token_from_db(store)
    
    if not access_token:
        app_logger.error(f'No access token found for store: {store}')
        raise StoreNotFoundException
    
    url = f'https://{store}.myshopify.com/admin/api/2023-04/graphql.json'
    headers = {
        'Content-Type': 'application/json',
        'X-Shopify-Access-Token': access_token,
    }
    
    app_logger.info(f'Sending request to Shopify API to update product with ID: {product_id} for store: {store}')
    

    query = f'mutation {{ productUpdate(input: {{id: "gid://shopify/Product/{product_id}", title: "{title}", bodyHtml: "{description}"}}) {{ product {{ id }} }} }}'
    data = {"query": query}
    
    app_logger.info(f'Request body: {data}')
       

    response = requests.post(url, headers=headers, data=json.dumps(data))
    
    app_logger.info(f'Shopify API Response: {response.json()}')
    app_logger.info(f'Shopify API Response Status Code: {response.status_code}')
    
    if response.status_code == 200:
        print(response.json())
    
        if response.json()['data']['productUpdate']['product'] == None:
            app_logger.warning(f'Failed to update product from Shopify API. Response: {response.json()}')
            app_logger.warning(f'Most Likely Reason is the The ID is not correct')
            print(f'Error updating product. Status code: {response.status_code}, Response: {response.text}')
            return False
    
        try:
            returned_id = int(response.json()['data']['productUpdate']['product']['id'].split('/')[-1])
        except:
            app_logger.warning(f'Failed to extract product ID from Response')
            app_logger.warning(f'Error updating product. Status code: {response.status_code}, Response: {response.text}')
            return False
        

        if returned_id == int(product_id):
            app_logger.info(f'Updated product with ID {product_id} from Shopify API')
            return True
        else:
            app_logger.warning(f'Failed to update product from Shopify API. Status Code: {response.status_code} ,  Response: {response.text}')
            print(f'Error updating product. Status code: {response.status_code}, Response: {response.text}')
            app_logger.warning(f"{returned_id} != {product_id}")
            app_logger.warning(f"{type(returned_id)} != {type(product_id)}")
            return False
    else:
        app_logger.warning(f'Failed to update product from Shopify API. Status Code: {response.status_code} ,  Response: {response.text}')
        print(f'Error updating product. Status code: {response.status_code}, Response: {response.text}')
        return False    
    

