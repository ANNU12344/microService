import requests
from src.Interactor.Dto.order_dto import order_dto
from src.Interactor.Logger.custom_logger import app_logger
def get_order_info(order_id):
    access_token=" "
    if not access_token:
        print("you don't have access to get the order info")
    app_logger.info(f'Sending request to WIX API to get oder info : {order_id}')
    url=f"https://www.wixapis.com/stores/v2/orders/{order_id}"
    headers={
        'X-Wix-Access-Token':access_token
    }
    orders = []
    response=requests.get(url,headers=headers)
    if response.status_code == 200:
        order_data = response.json().get('order', {})
        orders.append(order_dto(response))

    