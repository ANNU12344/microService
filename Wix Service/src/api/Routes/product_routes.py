from flask import request, jsonify
from flask_restx import Resource, reqparse, Namespace
from src.Interactor.Logger.custom_logger import app_logger
from src.Interactor.DTR.product_dtr import product_rest_response
import traceback

product_ns = Namespace('wix_rest', description='Wix Rest APIs')
product_parser = reqparse.RequestParser()
product_parser.add_argument('Authorization', type=str, location='headers', help='Authorization header', required=True)
product_parser.add_argument('product_id', type=str, help="product id", required=True)

@product_ns.route('/product/', methods=['GET'])
class Product(Resource):
    @product_ns.expect(product_parser)
    def get(self):  
        app_logger.info('Received request to get product')
        app_logger.info(f'Request headers: {request.headers}')
        args = request.get_json()
        product_id = args['product_id'] 
        try:
            response = product_rest_response(product_id)
        except Exception as e:
            exception_track = traceback.format_exc()
            app_logger.error(f'An unexpected error occurred: {e}')
            app_logger.error(f'An unexpected error occurred: {exception_track}')
            return jsonify({'message': f'Internal Server Error , {exception_track}'})
        return response
