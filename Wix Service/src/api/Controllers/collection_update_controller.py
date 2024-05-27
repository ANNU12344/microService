import requests
import json
from src.Interactor.Exception.custom_exceptions import SiteNotFoundException
from src.Interactor.Logger.custom_logger import app_logger
from src.api.Controllers.token_controller import get_token_from_db
def update_collections(wix_site,collection_id,name,description):
    access_token=get_token_from_db(wix_site)
    if not access_token:
        app_logger.error(f'No access token found for site')
        raise SiteNotFoundException
    
    url = f'https://www.wixapis.com/stores/v1/collections/{collection_id}'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': access_token
        
    }
    app_logger.info(f'Sending request to Wix API to update collection with ID: {collection_id} for wix site :{wix_site}')
    payload = json.dumps({
    "product": {
    "name": name,
    "description": description
    }
    })

    app_logger.info(f'Request body: {payload}')
    response = requests.patch(url, headers=headers, data=payload)

    
    app_logger.info(f'Wix API Response Status Code: {response.status_code}')

    if response.status_code == 200:
        print(response.json())
    
        if response.json()['product'] == None:
            app_logger.warning(f'Failed to update collection from Wix API. Response')
            app_logger.warning(f'Most Likely Reason is the The ID is not correct')
            print(f'Error updating collection. Status code: {response.status_code}, Response: {response.text}')
            return False
    
        try:
            data = response.json()
            returned_id =data['collection']['id']
            print(returned_id)

        except:
            app_logger.warning(f'Failed to extract collection ID from Response')
            app_logger.warning(f'Error updating collection. Status code: {response.status_code}, Response: {response.text}')
            return False
        

        if returned_id == collection_id:
            app_logger.info(f'Updated product with ID {collection_id} from Wix API')
            return True
        else:
            app_logger.warning(f'Failed to update collection from Wix API. Status Code: {response.status_code} ,  Response: {response.text}')
            print(f'Error updating collection. Status code: {response.status_code}, Response: {response.text}')
            app_logger.warning(f"{returned_id} != {collection_id}")
            app_logger.warning(f"{type(returned_id)} != {type(collection_id)}")
            return False
    else:
        app_logger.warning(f'Failed to update collection from Wix API. Status Code: {response.status_code} ,  Response: {response.text}')
        print(f'Error updating collection. Status code: {response.status_code}, Response: {response.text}')
        return False 