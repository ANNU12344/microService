from flask import request, jsonify
from flask_restx import Resource, reqparse, Namespace, fields
from src.Interactor.Logger.custom_logger import app_logger
from src.api.Controllers.collection_controller import create_collection_rest_response
from src.api.Auth.jwt import jwt_wrapper
import traceback


create_collection_ns = Namespace('wix_rest', description='Wix Rest APIs')

create_parser = reqparse.RequestParser()
create_parser.add_argument('Authorization', type=str, location='headers', help='Authorization header', required=True)
create_parser.add_argument('wix_site', type=str, help="wix site Name.", required=True)
create_parser.add_argument('name', type=str, help="name", required=True)
create_parser.add_argument('discription', type=str, help="product id", required=True)

@create_collection_ns.route('/create_collection')
class Collection(Resource):
    @create_collection_ns.expect(create_parser)
    def post(self):
        app_logger.info('Received request to create the collection')
        app_logger.info(f'Request headers: {request.headers}')
        app_logger.info(f'Request body: {request.get_json()}')

        args = create_parser.parse_args()
        wix_site = args['wix_site']
        name=args['name']
        discription=args['discription']
        

        try:
            if not wix_site:
                return jsonify({'message': 'wix_site is required'}), 400

            response = create_collection_rest_response(wix_site, name,discription)
        except Exception as e:
            exception_track = traceback.format_exc()
            app_logger.error(f'An unexpected error occurred: {e}')
            app_logger.error(f'Stack trace: {exception_track}')
            return jsonify({'message': f'Internal Server Error, {exception_track}'}), 500

        return response
