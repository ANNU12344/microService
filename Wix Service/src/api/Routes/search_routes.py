from flask import request, jsonify
from flask_restx import Resource, reqparse, Namespace
from src.Interactor.Logger.custom_logger import app_logger
from src.Interactor.DTR.search_dtr import search_rest_response
import traceback

search_ns = Namespace('wix_rest', description='wix Rest APIs')

search_parser = reqparse.RequestParser()
search_parser.add_argument('Authorization', type=str, location='headers', help='Authorization header', required=True)
search_parser.add_argument('optionType', type=str, help="Get Product Options Availability", required=True)
search_parser.add_argument('Name', type=str, help="Get Product Options Availability", required=True)
search_parser.add_argument('product_id', type=str, help="product id", required=True)


@search_ns.route('/search')
class Search(Resource):
    @search_ns.expect(search_parser)
    def get(self):
        app_logger.info('Received request to search Products')
        app_logger.info(f'Request headers: {request.headers}')
        app_logger.info(f'Request body: {request.get_json()}') 
        
        args = request.get_json()
        optionType = args['optionType']
        Name = args['Name']
        product_id=args['product_id']
        try:
            response = search_rest_response(product_id,optionType,Name)
        except Exception as e:
            exception_track = traceback.format_exc()
            app_logger.error(f'An unexpected error occurred: {e}')
            app_logger.error(f'An unexpected error occurred: {exception_track}')
            return jsonify({'message': f'Internal Server Error , {exception_track}'})
        return response