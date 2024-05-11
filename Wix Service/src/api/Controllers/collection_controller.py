import json
import requests
from src.Interactor.Logger.custom_logger import app_logger
from src.Interactor.Exception.custom_exceptions import TokenNotFoundException,UnauthorizedApiException
from src.api.Controllers.token_controller import get_token_from_db
def get_collection_by_id(wix_site,collection_id):
    access_token = get_token_from_db(wix_site)
    
    if not access_token:
        app_logger.error(f'No access token found for wix site :{wix_site}')
        raise TokenNotFoundException
    
    url = f"https://www.wixapis.com/stores/v1/collections/{collection_id}?includeNumberOfProducts=true"
    headers = {
        'Authorization': access_token
        }
    
    app_logger.info(f'Sending request to Wix Api to get collection from the wix site:{wix_site}')
    response = requests.get(url, headers=headers)

    app_logger.info(f'Wix API Response: {response.json()}')
    app_logger.info(f'Wix API Response Status Code: {response.status_code}')
   
    if response.status_code==200:
        collection_data = response.json()
        return collection_data
    elif response.status_code==401:
        app_logger.error('Unauthorized API call. Invalid API key or access token.')
        app_logger.error('Update the access token')
        raise UnauthorizedApiException
    else:
        app_logger.warning(f'Failed to retrieve collection from Wix site. Status Code : {response.status_code}')
    return response

    