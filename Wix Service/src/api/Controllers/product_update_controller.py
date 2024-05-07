import requests
import json
from src.Interactor.Exception.custom_exceptions import UnauthorizedApiException , TokenNotFoundException
from src.Interactor.Logger.custom_logger import app_logger


def update_products(product_id,name,slug,productType,description,sku,ribbon):
    access_token = ""#I have checked it manully but i have to add to db
    if not access_token:
        app_logger.error(f'No access token found for store')
        raise TokenNotFoundException
    
    url = f'https://www.wixapis.com/stores/v1/products/{product_id}'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': access_token
        
    }
    app_logger.info(f'Sending request to Wix API to update product with ID: {product_id}')
    payload = json.dumps({
    "product": {
    "name": name,
    "slug":slug,
    "productType":productType,
    "description": description,
    "sku":sku,
    "ribbon":ribbon
    }
    })

    
    app_logger.info(f'Request body: {payload}')
    response = requests.patch(url, headers=headers, data=payload)
    app_logger.info(f'Wix API Response: {response.json()}')
    app_logger.info(f'Wix API Response Status Code: {response.status_code}')
    # response.raise_for_status()  # Raise an exception for HTTP errors
    # collection_data = response.json()
    # app_logger.info(f'Successfully retrieved collection details: {collection_data}')
    # return collection_data
    if response.status_code == 200:
        print(response.json())
    
        if response.json()['product'] == None:
            app_logger.warning(f'Failed to update product from Wix API. Response: {response.json()}')
            app_logger.warning(f'Most Likely Reason is the The ID is not correct')
            print(f'Error updating product. Status code: {response.status_code}, Response: {response.text}')
            return False
    
        try:
            data = response.json()
            returned_id =data['product']['id']
            print(product_id)

        except:
            app_logger.warning(f'Failed to extract product ID from Response')
            app_logger.warning(f'Error updating product. Status code: {response.status_code}, Response: {response.text}')
            return False
        

        if returned_id == product_id:
            app_logger.info(f'Updated product with ID {product_id} from Wix API')
            return True
        else:
            app_logger.warning(f'Failed to update product from Wix API. Status Code: {response.status_code} ,  Response: {response.text}')
            print(f'Error updating product. Status code: {response.status_code}, Response: {response.text}')
            app_logger.warning(f"{returned_id} != {product_id}")
            app_logger.warning(f"{type(returned_id)} != {type(product_id)}")
            return False
    else:
        app_logger.warning(f'Failed to update product from Wix API. Status Code: {response.status_code} ,  Response: {response.text}')
        print(f'Error updating product. Status code: {response.status_code}, Response: {response.text}')
        return False 