import requests,json
from src.Interactor.Dto.order_dto import order_dto
from src.api.Controllers.token_controller import get_token_from_db
from src.Interactor.Exception.custom_exceptions import SiteNotFoundException,UnauthorizedApiException
from src.Interactor.Logger.custom_logger import app_logger

    

def get_all_order(wix_site):
    access_token=get_token_from_db(wix_site)
    app_logger.info(f"Access token :{access_token}")
    if not access_token:
        app_logger.error(f'No access token found for wix site :{wix_site}')
        raise SiteNotFoundException
    
    url=f"https://www.wixapis.com/stores/v2/orders/query"
    headers={
        'Authorization':access_token
    }   
    app_logger.info(f'Sending request to wix  API to get all order for wix _site: {wix_site}')
    response = requests.post(url, headers=headers)

    app_logger.info(f'Wix API Response: {response.json()}')
    app_logger.info(f'Wix API Response Status Code: {response.status_code}')

    if response.status_code == 200:
        wix_order = [order_dto(order) for order in response.json().get('orders', [])]
        app_logger.info(f'Retrieved {len(wix_order)} order from wix API')
        return  wix_order
    elif response.status_code == 401:
        app_logger.error('Unauthorized API call. Invalid API key or access token.')
        raise UnauthorizedApiException
    
    app_logger.warning(f'Failed to retrieve orders from wix site. Status Code: {response.status_code}')
    return []
    

def get_order_by_id(wix_site,order_id):
    access_token=get_token_from_db(wix_site)
    app_logger.info(f"Access token :{access_token}")

    if not access_token:
        app_logger.error(f'No access token found for wix site :{wix_site}')
        raise SiteNotFoundException
    
    url=f'https://www.wixapis.com/stores/v2/orders/{order_id}'
    headers={
        'Authorization':access_token
    }  

    app_logger.info(f'Sending request to WIX site to get order info : {order_id}')
    response=requests.get(url,headers=headers)

    app_logger.info(f'Wix API Response: {response.json()}')
    app_logger.info(f'Wix API Response Status Code: {response.status_code}')
    orders = []
    if response.status_code==200:
        order_data = response.json().get('order', {})
        orders.append(order_dto(order_data))
        app_logger.info(f'Retrieved order with ID {order_id} from Wix API')

    elif response.status_code==401:
        app_logger.error('Unauthorized API call. Invalid API key or access token.')
        app_logger.error('Update the access token')
        raise UnauthorizedApiException
    else:
        app_logger.warning(f'Failed to retrieve order from Wix site. Status Code : {response.status_code}')
    return orders 

    