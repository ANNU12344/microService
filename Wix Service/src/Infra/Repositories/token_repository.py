from src.Interactor.Database.sql_alchemy import sqlalchemy_db as db
from src.api.Models.token_model import Token
from src.Interactor.Logger.custom_logger import app_logger
from sqlalchemy.exc import SQLAlchemyError

class TokenRepository:
    
    @staticmethod
    def create_token(wix_site,access_token,refresh_token):
        try:
            new_token = Token(wix_site=wix_site,access_token=access_token,refresh_token=refresh_token)
            app_logger.info(f'Adding token to database: {new_token}')
            db.session.add(new_token)
            db.session.commit()
            return new_token
        except SQLAlchemyError as e:
            app_logger.error(f'Error creating token: {e}')
            db.session.rollback()
            raise

    @staticmethod
    def get_token_by_wix_site(wix_site):
        try:
            app_logger.info(f'Retrieving token by wix site: {wix_site}')
            return Token.query.filter_by(wix_site=wix_site).first()
        except SQLAlchemyError as e:
            app_logger.error(f'Error retrieving token by wix_site: {e}')
            raise

    @staticmethod
    def get_all_tokens():
        try:
            app_logger.info('Retrieving all tokens')
            return Token.query.all()
        except SQLAlchemyError as e:
            app_logger.error(f'Error retrieving all tokens: {e}')
            raise

    @staticmethod
    def update_token(wix_site,access_token,refresh_token):
        try:
            token = Token.query.filter_by(wix_site=wix_site).first()
            app_logger.info(f'New access_token: {access_token}')
            if token:
                app_logger.info(f"exist token")
                token.wix_site =wix_site
                token.access_token = access_token
                token.refresh_token=refresh_token
                db.session.commit()
                app_logger.info(f'Updated token: {token}')
                return token
            return None
        except SQLAlchemyError as e:
            app_logger.error(f'Error updating token: {e}')
            db.session.rollback()
            raise

    @staticmethod
    def delete_token(token_id):
        try:
            token = Token.query.get(token_id)
            if token:
                db.session.delete(token)
                db.session.commit()
                app_logger.info(f'Deleted token with ID {token_id}')
                return True
            return False
        except SQLAlchemyError as e:
            app_logger.error(f'Error deleting token: {e}')
            db.session.rollback()
            raise