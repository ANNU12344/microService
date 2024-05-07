from flask import Blueprint, app, request, jsonify
from src.api.Controllers.product_update_controller import update_products
from src.Interactor.Logger.custom_logger import app_logger
from flask_restx import Api, Resource, reqparse, Namespace,fields
import traceback


update_ns = Namespace('Wix_rest',  description='Wix Rest APIs')

update_parser = reqparse.RequestParser()
update_parser.add_argument('Authorization', type=str, location='headers', help='Authorization header', required=True)
update_parser.add_argument('product_id', type=str, help="Product / Category ID.", required=True)
update_parser.add_argument('name', type=str, help="New Title.", required=True)
update_parser.add_argument('slug', type=str, help="slug", required=True)
update_parser.add_argument('productType', type=str, help="Product Type", required=True)
update_parser.add_argument('description', type=str, help="Description of product", required=True)
update_parser.add_argument('sku', type=str, help="sku", required=True)
update_parser.add_argument('ribbon', type=str, help="ribbon", required=True)

@update_ns.route('/update_product')
class UpdateProduct(Resource):
    @update_ns.expect(update_parser)
    def post(self):
        app_logger.info('Received request to update product')
        app_logger.info(f'Request headers: {request.headers}')
        app_logger.info(f'Request body: {request.get_json()}') 
        args = request.get_json()
        product_id = args['product_id']
        name = args['name']
        slug=args['slug']
        productType=args['productType']
        description=args['description']
        sku=args['sku']
        ribbon=args['ribbon']
        app_logger.info(f'product Id:{product_id}')
        app_logger.info({name})
        
        try:
            update_status = update_products(product_id,name,slug,productType,description,sku,ribbon)
        except Exception as e:
            exception_track = traceback.format_exc()
            app_logger.error(f'An unexpected error occurred: {e}')
            app_logger.error(f'An unexpected error occurred: {exception_track}')
            return jsonify({'message': f'Internal Server Error , {exception_track}'})

        response = {"status": update_status}
        
        return jsonify(response)