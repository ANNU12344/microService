import requests
from src.Interactor.Dto.order_dto import order_dto
from src.api.Controllers.token_controller import get_token_from_db
from src.Interactor.Exception.custom_exceptions import TokenNotFoundException,UnauthorizedApiException
from src.Interactor.Logger.custom_logger import app_logger
def get_order_by_id(wix_site,order_id):
    access_token=get_token_from_db(wix_site)

    if not access_token:
        app_logger.error(f'No access token found for wix site :{wix_site}')
        raise TokenNotFoundException
    url=f"https://www.wixapis.com/stores/v2/orders/{order_id}"
    headers={
        'X-Wix-Access-Token':access_token
    }  

    app_logger.info(f'Sending request to WIX site to get order info : {order_id}')
    response=requests.get(url,headers=headers)

    app_logger.info(f'Wix API Response: {response.json()}')
    app_logger.info(f'Wix API Response Status Code: {response.status_code}')
   
    if response.status_code==200:
        order_data= response.json()
        # I have to modify here how to use the mapper to map with the entities like for that I am working with entities
        return order_data
    elif response.status_code==401:
        app_logger.error('Unauthorized API call. Invalid API key or access token.')
        app_logger.error('Update the access token')
        raise UnauthorizedApiException
    else:
        app_logger.warning(f'Failed to retrieve collection from Wix site. Status Code : {response.status_code}')
    return response

    