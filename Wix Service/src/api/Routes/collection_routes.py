from flask import request, jsonify
from flask_restx import Resource, reqparse, Namespace
from src.Interactor.Logger.custom_logger import app_logger
from src.Interactor.DTR.collection_dtr import collection_rest_response
import traceback

collection_ns = Namespace('wix_token', description='create the collection')
collection_parser = reqparse.RequestParser()
collection_parser.add_argument('Authorization', type=str, location='headers', help='Authorization header', required=True)
collection_parser.add_argument('collection_id', type=str, help="Collection ids", required=True)

@collection_ns .route('/collection/<collection_id>', methods=['GET'])
class Product(Resource):
    @collection_ns.expect(collection_parser)
    def get(self, collection_id):  
        app_logger.info('Received request to get collections')
        app_logger.info(f'Request headers: {request.headers}')
        try:
            response = collection_rest_response(collection_id)
        except Exception as e:
            exception_track = traceback.format_exc()
            app_logger.error(f'An unexpected error occurred: {e}')
            app_logger.error(f'An unexpected error occurred: {exception_track}')
            return jsonify({'message': f'Internal Server Error , {exception_track}'})
        return response
