from src.Domain.Entities.configuration import Configuration
from src.api.Controllers.site_data_controller import get_site_data
from src.Domain.Constant.constant import Platform_name , Platfrom_id
from src.Interactor.Logger.custom_logger import app_logger
from src.Domain.Event_Loop.loop_init import loop
from datetime import datetime
import requests
import aiohttp


async def _create_configuration(wix_site , token):
    try:
        app_logger.info(f"Creating configuration for wix site: {wix_site}")
        site_data = get_site_data(wix_site , token)
        today = datetime.now()

        # Create Configuration object
        configuration = Configuration(
            store_id="site_data['properties']['categories']['businessTermID']",
            businessName=site_data['properties']['businessName'],
            site_display_name=site_data['properties']['siteDisplayName'],
            platform_name=Platform_name,
            platform_id=Platfrom_id,
            auth_token=token,
            is_active=True,
            created_on=today
        )

        url = f""# I have to define the server url for create the configuration

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



def create_configuration(wix_site, token):   
    try: 
        loop.run_until_complete(_create_configuration(wix_site, token))
    except:
        app_logger.error(f"Failed to create configuration")