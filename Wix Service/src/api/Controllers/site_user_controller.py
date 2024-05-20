from src.Domain.Entities.site_user import SiteUser
from src.api.Controllers.site_data_controller import get_site_data
from src.Domain.Constant.constant import Platform_name , Platfrom_id
from src.Interactor.Logger.custom_logger import app_logger
from src.Domain.Event_Loop.loop_init import loop

from datetime import datetime
import requests
import aiohttp

version = "1.0"


async def _create_site_user(wix_site , token):
    try:
        app_logger.info(f"Creating site user for wix Site: {wix_site}")

        # Fetch shop data
        site_data = get_site_data(wix_site , token)

        today = datetime.now()

        # Create Store User object
        site_user = SiteUser(
            email=site_data.email,
            active=True,
            store_id=site_data.id,
            created_on=today,
            last_login_time=today,
            app_id=Platfrom_id,
            platform_id=Platfrom_id
        )

        url = f"" #i have to set this url

        headers = {
            'accept': 'text/plain',
            'Content-Type': 'application/json',
        }

        data = site_user.serialize()

        app_logger.info(f"Sending POST request to {url}")
         

        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, json=data) as response:
                if response.status == 200:
                    app_logger.info("Site User created successfully")
                else:
                    app_logger.error(f"Failed to create site user. Response status code: {response.status}, Response content: {await response.text()}")

    except Exception as e:
        app_logger.error(f"An unexpected error occurred: {e}")



def create_site_user(store_name, token):   
    try: 
        loop.run_until_complete(_create_site_user(store_name, token))
    except:
        app_logger.error(f"Failed to create configuration")
        
   