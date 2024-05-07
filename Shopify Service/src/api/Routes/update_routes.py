from flask import Blueprint, app, request, jsonify
from src.api.Controllers.product_update_controller import update_products
from src.api.Controllers.collection_update_controller import update_collections
from src.Interactor.Logger.custom_logger import app_logger
from flask_restx import Api, Resource, reqparse, Namespace,fields
from src.api.Auth.jwt import jwt_wrapper
import traceback


update_ns = Namespace('shopify_rest',  description='Shopify Rest APIs')

update_parser = reqparse.RequestParser()
update_parser.add_argument('Authorization', type=str, location='headers', help='Authorization header', required=True)
update_parser.add_argument('store_name', type=str, help="Store Name.", required=True)
update_parser.add_argument('id', type=str, help="Product / Category ID.", required=True)
update_parser.add_argument('title', type=str, help="New Title.", required=True)
update_parser.add_argument('description', type=str, help="New Description.", required=True)


@update_ns.route('/update_product')
class UpdateProduct(Resource):
    @update_ns.expect(update_parser)
    @jwt_wrapper
    def post(self):
        
        app_logger.info('Received request to update product')
        app_logger.info(f'Request headers: {request.headers}')
        app_logger.info(f'Request body: {request.get_json()}') 
        
        args = request.get_json()
        store_name = args['store_name']
        product_id = args['id']
        title = args['title']
        description = args['description']
        
        try:
            update_status = update_products(store_name, product_id, title, description)
        except Exception as e:
            exception_track = traceback.format_exc()
            app_logger.error(f'An unexpected error occurred: {e}')
            app_logger.error(f'An unexpected error occurred: {exception_track}')
            return jsonify({'message': f'Internal Server Error , {exception_track}'})

        response = {"status": update_status}
        
        return jsonify(response)
    
@update_ns.route('/update_collection')
class UpdateCategory(Resource):
    @update_ns.expect(update_parser)
    @jwt_wrapper
    def post(self):
        
        app_logger.info('Received request to update category')
        app_logger.info(f'Request headers: {request.headers}')
        app_logger.info(f'Request body: {request.get_json()}') 
        
        args = request.get_json()
        store_name = args['store_name']
        collection_id = args['id']
        title = args['title']
        description = args['description']

        try:
            update_status = update_collections(store_name, collection_id, title, description)
        except Exception as e:
            exception_track = traceback.format_exc()
            app_logger.error(f'An unexpected error occurred: {e}')
            app_logger.error(f'An unexpected error occurred: {exception_track}')
            return jsonify({'message': f'Internal Server Error , {exception_track}'})

        response = {"status": update_status}
        
        return jsonify(response)


