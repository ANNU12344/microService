from src.Domain.Entities.configuration import Configuration
from src.Infra.Repositories.token_repository import TokenRepository
from src.api.Controllers.shop_data_controller import get_shop_data
from src.Domain.Constant.constant import Platform_name , Platfrom_id
from src.Interactor.Logger.custom_logger import app_logger
from src.Domain.Event_Loop.loop_init import loop

from datetime import datetime
import requests
import aiohttp





version = "1.0"


async def _create_configuration(store_name , token):
    try:
        app_logger.info(f"Creating configuration for store: {store_name}")

        # Fetch shop data
        shop_data = get_shop_data(store_name , token)

        today = datetime.now()

        # Create Configuration object
        configuration = Configuration(
            store_id=shop_data.id,
            email=shop_data.email,
            store_name=shop_data.name,
            platform_name=Platform_name,
            platform_id=Platfrom_id,
            auth_token=token,
            is_active=True,
            created_on=today
        )

        url = f"http://103.127.29.218:7070/api/v{version}/Configuration"

        headers = {
            'accept': 'text/plain',
            'Content-Type': 'application/json',
        }

        data = configuration.serialize()

        app_logger.info(f"Sending POST request to {url}")
         

        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, json=data) as response:
                if response.status == 200:
                    app_logger.info("Configuration created successfully")
                else:
                    app_logger.error(f"Failed to create configuration. Response status code: {response.status}, Response content: {await response.text()}")

    except Exception as e:
        app_logger.error(f"An unexpected error occurred: {e}")



def create_configuration(store_name, token):   
    try: 
        loop.run_until_complete(_create_configuration(store_name, token))
    except:
        app_logger.error(f"Failed to create configuration")
        
   