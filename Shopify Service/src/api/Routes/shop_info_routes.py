from flask import request, jsonify
from src.Interactor.DTR.shop_dtr import shop_rest_response
from src.api.Auth.jwt import jwt_wrapper
from src.Interactor.Logger.custom_logger import app_logger
from flask_restx import Resource, reqparse, Namespace
import traceback



shop_info_ns = Namespace('shopify_rest', description='Shopify Rest APIs')

shop_info_parser = reqparse.RequestParser()
shop_info_parser.add_argument('Authorization', type=str, location='headers', help='Authorization header', required=True)
shop_info_parser.add_argument('store_name', type=str, help="Store Name.", required=True)

@shop_info_ns.route('/shop_info')
class ShopInfo(Resource):
    @shop_info_ns.expect(shop_info_parser)
    @jwt_wrapper
    def get(self):

        app_logger.info('Received request to get Store Info')
        app_logger.info(f'Request headers: {request.headers}')
        app_logger.info(f'Request body: {request.get_json()}') 
        
        args = request.get_json()
        store_name = args['store_name']
        
        try:
            response = shop_rest_response(store_name)
        except Exception as e:
            exception_track = traceback.format_exc()
            app_logger.error(f'An unexpected error occurred: {e}')
            app_logger.error(f'An unexpected error occurred: {exception_track}')
            return jsonify({'message': f'Internal Server Error , {exception_track}'})
        return response

    
    
