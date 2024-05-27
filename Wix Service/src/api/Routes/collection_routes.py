from flask import request, jsonify
from flask_restx import Resource, reqparse, Namespace
from src.Interactor.Logger.custom_logger import app_logger
from src.Interactor.DTR.collection_dtr import collection_rest_response
from src.api.Auth.jwt import jwt_wrapper
import traceback

collection_ns = Namespace('wix_rest', description='Wix Rest APIs')

collection_parser = reqparse.RequestParser()
collection_parser.add_argument('Authorization', type=str, location='headers', help='Authorization header', required=True)
collection_parser.add_argument('wix_site', type=str, help="wix site Name.", required=True)
collection_parser.add_argument('collection_id', type=str, help="collection id", required=True)

@collection_ns .route('/collection')
class Product(Resource):
    @collection_ns.expect(collection_parser)
    #@jwt_wrapper
    def get(self):

        app_logger.info('Received request to get Collection')
        app_logger.info(f'Request headers: {request.headers}')
        app_logger.info(f'Request body: {request.get_json()}') 

        args = request.get_json()
        wix_site = args['wix_site'] 
        collection_id = args['collection_id'] 
        

        if not isinstance(collection_id, str):
            return jsonify({'message': 'Invalid data format. Expected a collection_id.'})
        try:
            response = collection_rest_response(wix_site,collection_id)
        except Exception as e:
            exception_track = traceback.format_exc()
            app_logger.error(f'An unexpected error occurred: {e}')
            app_logger.error(f'An unexpected error occurred: {exception_track}')
            return jsonify({'message': f'Internal Server Error , {exception_track}'})
        return response
