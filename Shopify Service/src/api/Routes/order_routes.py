from flask import request, jsonify
from src.Interactor.DTR.order_dtr import order_rest_response
from src.Interactor.Logger.custom_logger import app_logger
from src.api.Auth.jwt import jwt_wrapper
from flask_restx import Resource, reqparse, Namespace
import traceback


order_ns = Namespace('shopify_rest', description='Shopify Rest APIs')

order_parser = reqparse.RequestParser()
order_parser.add_argument('Authorization', type=str, location='headers', help='Authorization header', required=True)
order_parser.add_argument('store_name', type=str, help="Store Name.", required=True)
order_parser.add_argument('order_ids', type=list, help="List of Order IDs.", required=True)


@order_ns.route('/orders')
class Order(Resource):
    @order_ns.expect(order_parser)
    @jwt_wrapper
    def get(self):
        

        app_logger.info('Received request to generate anything post')
        app_logger.info(f'Request headers: {request.headers}')
        app_logger.info(f'Request body: {request.get_json()}') 
        
        args = request.get_json()
        store_name = args['store_name']
        order_ids = args['order_ids']

        if not isinstance(order_ids, list):
            return jsonify({'message': 'Invalid data format. Expected a list of order_ids.'})
        
        try:
            response =  order_rest_response(store_name, order_ids)
        except Exception as e:
            exception_track = traceback.format_exc()
            app_logger.error(f'An unexpected error occurred: {e}')
            app_logger.error(f'An unexpected error occurred: {exception_track}')
            return jsonify({'message': f'Internal Server Error , {exception_track}'})
        return response


    
    
