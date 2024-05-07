from email.policy import default
from flask import request, jsonify
from flask_restx import Resource, reqparse, Namespace
from src.Interactor.Logger.custom_logger import app_logger
from src.api.Auth.jwt import jwt_wrapper
from src.Interactor.DTR.product_dtr import product_rest_response
import traceback


product_ns = Namespace('shopify_rest', description='Shopify Rest APIs')

product_parser = reqparse.RequestParser()
product_parser.add_argument('Authorization', type=str, location='headers', help='Authorization header', required=True)
product_parser.add_argument('store_name', type=str, help="Store Name.", required=True)
product_parser.add_argument('product_ids', type=list, help="List of Product IDs.",default = [] , required=True)


@product_ns.route('/products')
class Product(Resource):
    @product_ns.expect(product_parser)
    @jwt_wrapper
    def get(self):
        

        app_logger.info('Received request to get Products')
        app_logger.info(f'Request headers: {request.headers}')
        app_logger.info(f'Request body: {request.get_json()}') 
        

        args = request.get_json()
        #args = product_parser.parse_args(req=request)
        store_name = args['store_name']
        product_ids = args['product_ids']

        if not isinstance(product_ids, list):
            return jsonify({'message': 'Invalid data format. Expected a list of product_ids.'}) , 501

            
        try:
            response = product_rest_response(store_name, product_ids)
        except Exception as e:
            exception_track = traceback.format_exc()
            app_logger.error(f'An unexpected error occurred: {e}')
            app_logger.error(f'An unexpected error occurred: {exception_track}')
            return jsonify({'message': f'Internal Server Error , {exception_track}'})
        return response


    
    
