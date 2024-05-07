from flask import request, jsonify
from flask_restx import Resource, reqparse, Namespace
from src.Interactor.Logger.custom_logger import app_logger
from src.api.Auth.jwt import jwt_wrapper
from src.Interactor.DTR.search_dtr import search_rest_response
from src.Domain.Constant.constant import JWT_SECRET_KEY
import traceback

search_ns = Namespace('shopify_rest', description='Shopify Rest APIs')

search_parser = reqparse.RequestParser()
search_parser.add_argument('Authorization', type=str, location='headers', help='Authorization header', required=True)
search_parser.add_argument('store_name', type=str, help="Store Name.", required=True)
search_parser.add_argument('search_term', type=str, help="Search Term.", required=True)


@search_ns.route('/search')
class Search(Resource):
    @search_ns.expect(search_parser)
    @jwt_wrapper
    def get(self):
        

        app_logger.info('Received request to search Products')
        app_logger.info(f'Request headers: {request.headers}')
        app_logger.info(f'Request body: {request.get_json()}') 
        
        args = request.get_json()
        store_name = args['store_name']
        search_term = args['search_term']
        try:
            response = search_rest_response(store_name, search_term)
        except Exception as e:
            exception_track = traceback.format_exc()
            app_logger.error(f'An unexpected error occurred: {e}')
            app_logger.error(f'An unexpected error occurred: {exception_track}')
            return jsonify({'message': f'Internal Server Error , {exception_track}'})
        return response