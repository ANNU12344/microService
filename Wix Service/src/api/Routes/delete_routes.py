from flask import request, jsonify
from flask_restx import Resource, reqparse, Namespace
from src.Interactor.Logger.custom_logger import app_logger
from src.api.Auth.jwt import jwt_wrapper
from src.api.Controllers.product_controller import deleteProduct
from src.api.Controllers.collection_controller import deleteCollection
import traceback

delete_ns = Namespace('wix_rest', description='Wix Rest APIs')

delete_parser = reqparse.RequestParser()
delete_parser.add_argument('Authorization', type=str, location='headers', help='Authorization header', required=True)
delete_parser.add_argument('wix_site', type=str, help="wix site Name.", required=True)
delete_parser.add_argument('id', type=str, help="id", required=True)

@delete_ns.route('/product_delete')
class Product(Resource):
    @delete_ns.expect(delete_parser)
    # @jwt_wrapper
    def delete(self):

        app_logger.info('Received request  delete the product ')
        app_logger.info(f'Request headers: {request.headers}')
        app_logger.info(f'Request body: {request.get_json()}') 

        args = request.get_json()
        wix_site = args['wix_site'] 
        id = args['id']

        if not isinstance(id, str):
            return jsonify({'message': 'Invalid data format. Expected a collection_id.'})

        try:
            delete_status=deleteProduct(wix_site,id)
        except Exception as e:
            exception_track = traceback.format_exc()
            app_logger.error(f'An unexpected error occurred: {e}')
            app_logger.error(f'An unexpected error occurred: {exception_track}')
            return jsonify({'message': f'Internal Server Error , {exception_track}'})
        
        response = {"status": delete_status}
        
        return jsonify(response)
        


@delete_ns.route('/collection_delete')
class Product(Resource):
    @delete_ns.expect(delete_parser)
    # @jwt_wrapper
    def delete(self):

        app_logger.info('Received request to delete Collection')
        app_logger.info(f'Request headers: {request.headers}')
        app_logger.info(f'Request body: {request.get_json()}') 

        args = request.get_json()
        wix_site = args['wix_site'] 
        id = args['id'] 
        
        if not isinstance(id, str):
            return jsonify({'message': 'Invalid data format. Expected a collection_id.'})
        try:
            delete_status=deleteCollection(wix_site,id)
            # return jsonify(response)
        except Exception as e:
            exception_track = traceback.format_exc()
            app_logger.error(f'An unexpected error occurred: {e}')
            app_logger.error(f'An unexpected error occurred: {exception_track}')
            return jsonify({'message': f'Internal Server Error , {exception_track}'})
        
        response = {"status": delete_status}
        
        return jsonify(response)
        
       

        