from flask import request, jsonify
from src.Interactor.DTR.shop_dtr import is_active_rest_response
from src.api.Auth.jwt import jwt_wrapper
from src.Interactor.Logger.custom_logger import app_logger
from flask_restx import Resource, reqparse, Namespace
import traceback

isActive_ns = Namespace('shopify_rest', description='Shopify Rest APIs')

isActive_parser = reqparse.RequestParser()
isActive_parser.add_argument('Authorization', type=str, location='headers', help='Authorization header', required=True)
isActive_parser.add_argument('store_name', type=str, help="Store Name.", required=True)

@isActive_ns.route('/isActive')
class isActive(Resource):
    @isActive_ns.expect(isActive_parser)
    @jwt_wrapper
    def get(self):

        app_logger.info('Received request to get Store Info')
        app_logger.info(f'Request headers: {request.headers}')
        app_logger.info(f'Request body: {request.get_json()}') 
        
        args = request.get_json()
        store_name = args['store_name']
        
        try:
            response = is_active_rest_response(store_name)
        except Exception as e:
            exception_track = traceback.format_exc()
            app_logger.error(f'An unexpected error occurred: {e}')
            app_logger.error(f'An unexpected error occurred: {exception_track}')
            return jsonify({'message': f'Internal Server Error , {exception_track}'})
        return response