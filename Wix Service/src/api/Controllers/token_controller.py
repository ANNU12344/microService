from src.Infra.Repositories.token_repository import TokenRepository
from src.Interactor.Exception.custom_exceptions import UnauthorizedApiException , TokenNotFoundException
from src.Interactor.Logger.custom_logger import app_logger

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
    