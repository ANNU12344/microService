from flask import request, jsonify
from flask_restx import Resource, reqparse, Namespace
from src.Interactor.Logger.custom_logger import app_logger
from src.Interactor.DTR.post_dtr import post_rest_response
from src.api.Auth.jwt import jwt_wrapper
import traceback

post_ns = Namespace('wix_rest', description='Wix Rest APIs')

post_parser = reqparse.RequestParser()
post_parser.add_argument('Authorization', type=str, location='headers', help='Authorization header', required=True)
post_parser.add_argument('wix_site', type=str, help="wix site Name.", required=True)
post_parser.add_argument('post_ids', type=str, help="post ids", required=True)

@post_ns .route('/posts')
class Post(Resource):
    @post_ns.expect(post_parser)
    # @jwt_wrapper
    def get(self):

        app_logger.info('Received request to get Posts')
        app_logger.info(f'Request headers: {request.headers}')
        app_logger.info(f'Request body: {request.get_json()}') 

        args = request.get_json()
        wix_site = args['wix_site'] 
        post_ids = args['post_ids'] 
        

        if not isinstance(post_ids, str):
            return jsonify({'message': 'Invalid data format. Expected a post_ids.'})
        try:
            response = post_rest_response(wix_site,post_ids)
        except Exception as e:
            exception_track = traceback.format_exc()
            app_logger.error(f'An unexpected error occurred: {e}')
            app_logger.error(f'An unexpected error occurred: {exception_track}')
            return jsonify({'message': f'Internal Server Error , {exception_track}'})
        return response
