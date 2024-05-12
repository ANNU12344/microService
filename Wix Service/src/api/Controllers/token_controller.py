from src.Infra.Repositories.token_repository import TokenRepository
from src.Interactor.Exception.custom_exceptions import UnauthorizedApiException , TokenNotFoundException
from src.Interactor.Logger.custom_logger import app_logger
import logging
from requests.exceptions import HTTPError
import os,requests
from dotenv import load_dotenv
load_dotenv()
APP_ID = os.environ.get('APP_ID')
APP_SECRET_KEY= os.environ.get('APP_SECRET_KEY')

def get_token_from_db(wix_site):
    print(f'Getting token from database for Wix_site: {wix_site}')
    token_repo = TokenRepository().get_token_by_wix_site(wix_site)
    app_logger.info(f'Found token: {token_repo}')
    if token_repo != None:
        app_logger.info(f'Serializing token')
        token = token_repo.serialize()['access_token']
        return token
    else:
        app_logger.warning(f'No token found for store: {wix_site}')
        return None
    

def token_exist(wix_site):
    app_logger.info(f'Checking if token exists for store: {wix_site}')
    if get_token_from_db(wix_site) != None:
        app_logger.info(f'Token exists for store: {wix_site}')
        return True
    else:
        app_logger.warning(f'Token does not exist for wix site: {wix_site}')
        return False
    
def update_access_token(wix_site):
    token_repo = TokenRepository().get_token_by_wix_site(wix_site)
    app_logger.info(f'Found token: {token_repo}')
    if token_repo != None:
        app_logger.info(f'Serializing token')
        app_logger.info(f'APP id :{APP_ID}')
        app_logger.info(f'APP secret id :{APP_SECRET_KEY}')
        refresh_token = token_repo.serialize()['refresh_token']
        app_logger.info(f'Refresh token from the data base: {refresh_token}')
        url=f"https://www.wix.com/oauth/access"
        payload = {
            "client_id": APP_ID,
            "client_secret": APP_SECRET_KEY,
            "grant_type": "refresh_token",
            "refresh_token": refresh_token
        }
        try:
            response = requests.post(url, json=payload)
            app_logger.info(f'Response status :{response.status_code}')
            new_access_token=response.json()['access_token']
            app_logger.info(f'New Access Token: {new_access_token}')
            new_token=TokenRepository.update_token(wix_site,new_access_token,refresh_token)
            return "Updated"
        except HTTPError as ex:
            logging.exception(ex)
            return None


 