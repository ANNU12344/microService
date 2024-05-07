# from src.Interactor.Database.sql_alchemy import sqlalchemy_db as db
# from src.api.Models.token_model import Token
# from src.Interactor.Logger.custom_logger import app_logger
# from sqlalchemy.exc import SQLAlchemyError

# class TokenRepository:
    
#     def create_token(Consumer_key,Consumer_secret_key,access_oauth_token,access_oauth_token_secret,verify_code):
#         try:
#             new_token = Token(Consumer_key=Consumer_key,Consumer_secret_key=Consumer_secret_key,access_oauth_token=access_oauth_token,access_oauth_token_secret=access_oauth_token_secret,verify_code=verify_code)
#             app_logger.info(f'Adding token to database: {new_token}')
#             db.session.add(new_token)
#             db.session.commit()
#             return new_token
#         except SQLAlchemyError as e:
#             app_logger.error(f'Error creating token: {e}')
#             db.session.rollback()
#             raise

#     def get_token_by_key(self, consumer_key, consumer_secret_key):
#         token = Token.query.filter_by(Consumer_key=consumer_key, Consumer_secret_key=consumer_secret_key).first()
#         if token:
#             return token.serialize()
#         else:
#             return None