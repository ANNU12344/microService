from src.Domain.Entities.uninstall import Uninstall
from src.api.Controllers.shop_data_controller import get_shop_data
from src.Domain.Constant.constant import Platform_name , Platfrom_id
from src.Interactor.Logger.custom_logger import app_logger
from src.Domain.Event_Loop.loop_init import loop

from datetime import datetime
import requests
import aiohttp

version = "1.0"


async def _create_uninstall(store_name):
    try:
        app_logger.info(f"Creating uninstall for store: {store_name}")

        # Fetch shop data
        shop_data = get_shop_data(store_name)

        today = datetime.now()

        # Create Store User object
        uninstall = Uninstall(
            store_id=shop_data.id,
            store_name=shop_data.name,
            platform_id=Platfrom_id,
            platform_name=Platform_name
        )

        url = f"http://103.127.29.218:7070/api/v{version}/Uninstall"

        headers = {
            'accept': 'text/plain',
            'Content-Type': 'application/json',
        }

        data = uninstall.serialize()

        app_logger.info(f"Sending POST request to {url}")
         

        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, json=data) as response:
                if response.status == 200:
                    app_logger.info("Store User created successfully")
                else:
                    app_logger.error(f"Failed to create uninstall. Response status code: {response.status}, Response content: {await response.text()}")

    except Exception as e:
        app_logger.error(f"An unexpected error occurred: {e}")



def create_uninstall(store_name, token):   
    try: 
        loop.run_until_complete(_create_uninstall(store_name, token))
    except:
        app_logger.error(f"Failed to create configuration")
        
   