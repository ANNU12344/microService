import requests
import json
from src.Interactor.Logger.custom_logger import app_logger
from src.api.Controllers.token_controller import get_token_from_db
from src.Interactor.Exception.custom_exceptions import TokenNotFoundException,UnauthorizedApiException
def get_product_by_id(wix_site,product_id):
    access_token = get_token_from_db(wix_site)
   
    if not access_token:
        app_logger.error(f'No access token found for wix site :{wix_site}')
        raise TokenNotFoundException
    
    url = f"https://www.wixapis.com/stores-reader/v1/products/{product_id}"
    headers = {'Authorization': access_token}

    app_logger.info(f'Sending request to wix API to get product with ID: {product_id} for wix site: {wix_site}')
    response = requests.get(url, headers=headers)

    app_logger.info(f'Wix API Response Status Code: {response.status_code}')
   
    if response.status_code==200:
        product_data = response.json()
        return product_data
    elif response.status_code==401:
        app_logger.error('Unauthorized API call. Invalid API key or access token.')
        app_logger.error('Update the access token')
        raise UnauthorizedApiException
    else:
        app_logger.warning(f'Failed to retrieve product from Wix site. Status Code : {response.status_code}')
    return response
    

def get_Product_Options_Availability(product_id,optionType,Name):
    app_logger.info(f'Received request to check the product availability with optionType :{optionType} and Name :{Name}')
    # access_token = get_token_from_db(wix_site)
    access_token=""
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

    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        response.raise_for_status()  # Raise an exception for HTTP errors
        product_data = response.json()
        app_logger.info(f'Successfully retrieved product Availability details: {product_data}')
        return product_data 
    except requests.exceptions.RequestException as e:
        app_logger.error(f'Failed to retrieve product Availability details: {e}')
        return "Failed to retrieve product Availability details", 500


    
