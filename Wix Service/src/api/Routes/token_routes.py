from flask import request, jsonify
from src.api.Controllers.token_controller import get_token_from_db
from src.api.Controllers.token_controller import update_access_token
from src.api.Controllers.token_controller import token_exist
from src.Interactor.Logger.custom_logger import app_logger
from flask_restx import Resource, reqparse, Namespace
import traceback


token_ns = Namespace('wix_rest', description='Wix Rest APIs')

token_parser = reqparse.RequestParser()
token_parser.add_argument('Authorization', type=str, location='headers', help='Authorization header', required=True)
token_parser.add_argument('wix_site', type=str, location='form', help="Store Name", required=True)



@token_ns.route('/update_token')
class Token(Resource):
    @token_ns.expect(token_parser)
    def post(self):
        
        app_logger.info('Received request to get token')
        app_logger.info(f'Request headers: {request.headers}')
        app_logger.info(f'Request body: {request.get_json()}') 
    
        args = request.get_json()
        wix_site = args['wix_site']
        
        app_logger.info(f'Received request to get token for store: {wix_site}')
        
        try:
            if token_exist(wix_site):
                app_logger.info(f'Retrieved token for store: {wix_site}')
                response= update_access_token(wix_site)
                return jsonify({'message': 'Sucessfully Updated access token'})
        except Exception as e:
            exception_track = traceback.format_exc()
            app_logger.error(f'An unexpected error occurred: {e}')
            app_logger.error(f'An unexpected error occurred: {exception_track}')
            return jsonify({'message': f'Internal Server Error , {exception_track}'})

        return jsonify({'message': 'Token not found'}), 404