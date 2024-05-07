from src.Infra.Repositories.token_repository import TokenRepository
from src.Interactor.Exception.custom_exceptions import UnauthorizedApiException , StoreNotFoundException
from src.Interactor.Logger.custom_logger import app_logger

def get_token_from_db(store_name):
    app_logger.info(f'Getting token from database for store: {store_name}')
    token_repo = TokenRepository().get_token_by_store_name(store_name)
    app_logger.info(f'Found token: {token_repo}')
    if token_repo != None:
        app_logger.info(f'Serializing token')
        token = token_repo.serialize()['token']
        return token
    else:
        app_logger.warning(f'No token found for store: {store_name}')
        return None
    
    
def token_exist(store_name):
    app_logger.info(f'Checking if token exists for store: {store_name}')
    if get_token_from_db(store_name) != None:
        app_logger.info(f'Token exists for store: {store_name}')
        return True
    else:
        app_logger.warning(f'Token does not exist for store: {store_name}')
        return False
    return False