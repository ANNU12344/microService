from flask import request, jsonify
from src.api.Auth.jwt import jwt_wrapper
from src.Interactor.Logger.custom_logger import app_logger
from flask_restx import Resource, reqparse, Namespace
from src.Interactor.DTR.collection_dtr import collection_rest_response
import traceback

collection_ns = Namespace('shopify_rest', description='Shopify Rest APIs')

collection_parser = reqparse.RequestParser()
collection_parser.add_argument('Authorization', type=str, location='headers', help='Authorization header', required=True)
collection_parser.add_argument('store_name', type=str, help="Store Name.", required=True)
collection_parser.add_argument('collection_ids', type=list, help="List of Collection IDs.", required=True)

@collection_ns.route('/collection')
class Collection(Resource):
    @collection_ns.expect(collection_parser)
    @jwt_wrapper
    def get(self):
        

        app_logger.info('Received request to get Collections')
        app_logger.info(f'Request headers: {request.headers}')
        app_logger.info(f'Request body: {request.get_json()}') 
        
        args = request.get_json()
        store_name = args['store_name']
        collection_ids = args['collection_ids']

        if not isinstance(collection_ids, list):
            return jsonify({'message': 'Invalid data format. Expected a list of collection_ids.'})
        try:
            response = collection_rest_response(store_name, collection_ids)
        except Exception as e:
            exception_track = traceback.format_exc()
            app_logger.error(f'An unexpected error occurred: {e}')
            app_logger.error(f'An unexpected error occurred: {exception_track}')
            return jsonify({'message': f'Internal Server Error , {exception_track}'})
        return response

