import requests
import json
from src.Interactor.Logger.custom_logger import app_logger
from src.api.Controllers.token_controller import get_token_from_db
from src.Interactor.Dto.product_dto import product_dto
from src.Interactor.Exception.custom_exceptions import TokenNotFoundException,UnauthorizedApiException

def get_all_product(wix_site):
    access_token = get_token_from_db(wix_site)

    if not access_token:
        app_logger.error(f'No access token found for wix site :{wix_site}')
        raise TokenNotFoundException
    
    url = f"https://www.wixapis.com/stores/v1/products/query"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': access_token
        }
    app_logger.info(f'Sending request to wix  API to get all products for wix _site: {wix_site}')
    response = requests.post(url, headers=headers)

    app_logger.info(f'Wix API Response: {response.json()}')
    app_logger.info(f'Wix API Response Status Code: {response.status_code}')

    if response.status_code == 200:
        wix_products = [product_dto(product) for product in response.json().get('products', [])]
        app_logger.info(f'Retrieved {len(wix_products)} products from wix API')
        return  wix_products
    elif response.status_code == 401:
        app_logger.error('Unauthorized API call. Invalid API key or access token.')
        raise UnauthorizedApiException
    
    app_logger.warning(f'Failed to retrieve products from wix site. Status Code: {response.status_code}')
    return []


    
def get_product_by_id(wix_site,product_id):
    access_token = get_token_from_db(wix_site)

    if not access_token:
        app_logger.error(f'No access token found for wix site :{wix_site}')
        raise TokenNotFoundException
    
    products = []
    
    url = f"https://www.wixapis.com/stores-reader/v1/products/{product_id}"
    headers = {'Authorization': access_token}

    app_logger.info(f'Sending request to wix API to get product with ID: {product_id} for wix site: {wix_site}')
    response = requests.get(url, headers=headers)

    app_logger.info(f'Wix API Response: {response.json()}')
    app_logger.info(f'Wix API Response Status Code: {response.status_code}')
   
    if response.status_code==200:
        product_data = response.json().get('product', {})
        products.append(product_dto(product_data))
        app_logger.info(f'Retrieved product with ID {product_id} from Wix APIs')

    elif response.status_code==401:
        app_logger.error('Unauthorized API call. Invalid API key or access token.')
        app_logger.error('Update the access token')
        raise UnauthorizedApiException
    else:
        app_logger.warning(f'Failed to retrieve product from Wix site. Status Code : {response.status_code}')
    return products
    

    
def get_Product_Options_Availability(product_id,optionType,Name,wix_site):
    app_logger.info(f'Received request to check the product availability with optionType :{optionType} and Name :{Name}')
    access_token = get_token_from_db(wix_site)
    
    if not access_token:
        app_logger.error(f'No access token found for wix site :{wix_site}')
        raise TokenNotFoundException
    
    url=f"https://www.wixapis.com/stores-reader/v1/products/{product_id}/productOptionsAvailability"
    headers = {'Authorization': access_token}

    payload = json.dumps({
    "productOptions": [
        {
            "optionType": optionType,
            "name": Name,
        }
        ]
    })


    response = requests.request("POST", url, headers=headers, data=payload)
    app_logger.info(f'Wix API Response: {response.json()}')
    app_logger.info(f'Wix API Response Status Code: {response.status_code}')
    
    if response.status_code==200: 
        product_data = response.json()
        # I have to modify here how to use the mapper to map with the entities like for that I am working with entities
        app_logger.info(f'Product response: {product_data}')
        app_logger.info(f'Successfully retrieved product Availability details: {product_data}')
        return product_data
    elif response.status_code==401:
        app_logger.error('Unauthorized API call. Invalid API key or access token.')
        app_logger.error('Update the access token')
        raise UnauthorizedApiException
    else:
        app_logger.warning(f'Failed to retrieve product availability from Wix site. Status Code : {response.status_code}')
    return response


    
def deleteProduct(wix_site,id):
    access_token = get_token_from_db(wix_site)
    
    if not access_token:
        app_logger.error(f'No access token found for wix site :{wix_site}')
        raise TokenNotFoundException
    
    url=f'https://www.wixapis.com/stores/v1/products/{id}'

    headers = {'Authorization': access_token}
    response = requests.delete(url, headers=headers)
    app_logger.info(f'Request response: {response.status_code}')
    if response.status_code==200:
        return {}
    elif response.status_code==401:
        app_logger.error('Unauthorized API call. Invalid API key or access token.')
        app_logger.error('Update the access token')
        raise UnauthorizedApiException
    else:
        app_logger.warning(f'Failed to delete the product from the Wix site. Status Code : {response.status_code}')
    return {}
    

    

