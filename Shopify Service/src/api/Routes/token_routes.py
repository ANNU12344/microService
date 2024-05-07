from flask import request, jsonify
from src.api.Controllers.token_controller import get_token_from_db
from src.api.Controllers.token_controller import token_exist
from src.Interactor.Logger.custom_logger import app_logger
from src.api.Auth.jwt import jwt_wrapper
from flask_restx import Resource, reqparse, Namespace
import traceback






token_ns = Namespace('shopify_rest', description='Shopify Rest APIs')

token_parser = reqparse.RequestParser()
token_parser.add_argument('Authorization', type=str, location='headers', help='Authorization header', required=True)
token_parser.add_argument('store_name', type=str, location='form', help="Store Name", required=True)



@token_ns.route('/token')
class Token(Resource):
    @token_ns.expect(token_parser)
    @jwt_wrapper
    def get(self):
        

        app_logger.info('Received request to get token')
        app_logger.info(f'Request headers: {request.headers}')
        app_logger.info(f'Request body: {request.get_json()}') 
        
        print(request)
        args = request.get_json()
        store_name = args['store_name']
        
        app_logger.info(f'Received request to get token for store: {store_name}')
        
        try:
            if token_exist(store_name):
                app_logger.info(f'Retrieved token for store: {store_name}')
                return jsonify(get_token_from_db(store_name))
        except Exception as e:
            exception_track = traceback.format_exc()
            app_logger.error(f'An unexpected error occurred: {e}')
            app_logger.error(f'An unexpected error occurred: {exception_track}')
            return jsonify({'message': f'Internal Server Error , {exception_track}'})

        return jsonify({'message': 'Token not found'}), 404



    
