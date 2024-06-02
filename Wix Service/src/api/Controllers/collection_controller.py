from src.Interactor.Logger.custom_logger import app_logger
from src.Interactor.Dto.collection_dto import collection_dto
from src.Interactor.Exception.custom_exceptions import SiteNotFoundException,UnauthorizedApiException
from src.api.Controllers.token_controller import get_token_from_db
import requests,json

def create_collection_rest_response(wix_site, name,discription):
    access_token = get_token_from_db(wix_site)

    if not access_token:
        app_logger.error(f'No access token found for wix site :{wix_site}')
        raise SiteNotFoundException
    url = f"https://www.wixapis.com/stores/v1/collections"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': access_token
    }
    payload = json.dumps({
     "collection": {
    "name": name,
    "discription":discription
    }
    })
    response = requests.post(url, data=payload, headers=headers)
    app_logger.info(f'Wix API Response: {response.json()}')
    app_logger.info(f'Wix API Response Status Code: {response.status_code}')
    if response.status_code==200:
        collection_data = response.json().get('collection', {})
        return collection_data

    elif response.status_code==401:
        app_logger.error('Unauthorized API call. Invalid API key or access token.')
        app_logger.error('Update the access token')
        raise UnauthorizedApiException
    else:
        app_logger.warning(f'Failed to retrieve product from Wix site. Status Code : {response.status_code}')
    return []
    
    

def get_all_collection(wix_site):
    access_token = get_token_from_db(wix_site)

    if not access_token:
        app_logger.error(f'No access token found for wix site :{wix_site}')
        raise SiteNotFoundException
    
    url = f"https://www.wixapis.com/stores/v1/collections/query"
    headers = {
        'Authorization': access_token
        }
    app_logger.info(f'Sending request to wix  API to get all collection for wix _site: {wix_site}')
    response = requests.post(url, headers=headers)

    app_logger.info(f'Wix API Response: {response.json()}')
    app_logger.info(f'Wix API Response Status Code: {response.status_code}')

    if response.status_code == 200:
        wix_collection = [collection_dto(collection) for collection in response.json().get('collections', [])]
        app_logger.info(f'Retrieved {len(wix_collection)} collections from wix API')
        return  wix_collection
    elif response.status_code == 401:
        app_logger.error('Unauthorized API call. Invalid API key or access token.')
        raise UnauthorizedApiException
    
    app_logger.warning(f'Failed to retrieve collections from wix site. Status Code: {response.status_code}')
    return []
        

def get_collection_by_id(wix_site,collection_id):
    access_token = get_token_from_db(wix_site)

    if not access_token:
        app_logger.error(f'No access token found for wix site :{wix_site}')
        raise SiteNotFoundException
    
    collections = []
    
    url = f"https://www.wixapis.com/stores/v1/collections/{collection_id}?includeNumberOfProducts=true"
    headers = {
        'Authorization': access_token
        }
        
    app_logger.info(f'Sending request to Wix Api to get collection from the wix site:{wix_site}')
    response = requests.get(url, headers=headers)

    app_logger.info(f'Wix API Response: {response.json()}')
    app_logger.info(f'Wix API Response Status Code: {response.status_code}')
   
    if response.status_code==200:
        collection_data = response.json().get('collection', {})
        collections.append(collection_dto(collection_data))
        app_logger.info(f'Retrieved collection with ID {collection_id} from Wix API')
    elif response.status_code==401:
        app_logger.error('Unauthorized API call. Invalid API key or access token.')
        raise UnauthorizedApiException
    else:
        app_logger.warning(f'Failed to retrieve collection from Wix site. Status Code : {response.status_code}')
    return collections


def deleteCollection(wix_site,id):
    access_token = get_token_from_db(wix_site)
    
    if not access_token:
        app_logger.error(f'No access token found for wix site :{wix_site}')
        raise SiteNotFoundException
    
    url=f"https://www.wixapis.com/stores/v1/collections/{id}"
    headers = {'Authorization': access_token}

    response = requests.delete(url, headers=headers)
    app_logger.info(f'Wix response status :{response.status_code}')
    if response.status_code==200:
        return {}
    elif response.status_code==401:
        app_logger.error('Unauthorized API call. Invalid API key or access token.')
        app_logger.error('Update the access token')
        raise UnauthorizedApiException
    else:
        app_logger.warning(f'Failed to delete the collection from the Wix site. Status Code : {response.status_code}')
    return {}


    