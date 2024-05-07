# from src.Infra.Repositiories.token_repository import TokenRepository
# from src.Interactor.Logger.custom_logger import app_logger
# from src.api.Controllers.token_controller import get_token_from_db
# from src.Domain.Constant import constant
# from requests_oauthlib import OAuth1Session

# consumer_key=constant.TUMBLR_Consumer_Key
# consumer_secret=constant.TUMBLR_Secret_Key
# # def user_info_response():
    
    
    
    
# def token_exist(Consumer_key,Consumer_secret_key):
#     app_logger.info(f'Checking if token exists')
#     if get_token_from_db(Consumer_key,Consumer_secret_key) != None:
#         app_logger.info(f'Token exists for store: {Consumer_key,Consumer_secret_key}')
#         return True
#     else:
#         app_logger.warning(f'Token does not exist for store: {Consumer_key,Consumer_secret_key}')
#         return False
#     return False