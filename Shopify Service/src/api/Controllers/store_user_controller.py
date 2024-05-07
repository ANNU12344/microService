from src.Domain.Entities.store_user import StoreUser
from src.api.Controllers.shop_data_controller import get_shop_data
from src.Domain.Constant.constant import Platform_name , Platfrom_id
from src.Interactor.Logger.custom_logger import app_logger
from src.Domain.Event_Loop.loop_init import loop

from datetime import datetime
import requests
import aiohttp

version = "1.0"


async def _create_store_user(store_name , token):
    try:
        app_logger.info(f"Creating store user for store: {store_name}")

        # Fetch shop data
        shop_data = get_shop_data(store_name , token)

        today = datetime.now()

        # Create Store User object
        store_user = StoreUser(
            email=shop_data.email,
            active=True,
            store_id=shop_data.id,
            created_on=today,
            last_login_time=today,
            app_id=Platfrom_id,
            platform_id=Platfrom_id
        )

        url = f"http://103.127.29.218:7070/api/v{version}/StoreUser"

        headers = {
            'accept': 'text/plain',
            'Content-Type': 'application/json',
        }

        data = store_user.serialize()

        app_logger.info(f"Sending POST request to {url}")
         

        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, json=data) as response:
                if response.status == 200:
                    app_logger.info("Store User created successfully")
                else:
                    app_logger.error(f"Failed to create store user. Response status code: {response.status}, Response content: {await response.text()}")

    except Exception as e:
        app_logger.error(f"An unexpected error occurred: {e}")



def create_store_user(store_name, token):   
    try: 
        loop.run_until_complete(_create_store_user(store_name, token))
    except:
        app_logger.error(f"Failed to create configuration")
        
   