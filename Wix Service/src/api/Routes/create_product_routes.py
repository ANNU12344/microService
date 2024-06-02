from flask import request, jsonify
from flask_restx import Resource, reqparse, Namespace, fields
from src.Interactor.Logger.custom_logger import app_logger
from src.api.Controllers.product_controller import create_product_rest_response
from src.api.Auth.jwt import jwt_wrapper
import traceback


choices_type = fields.List(fields.Nested({
    'value': fields.String(required=True),
    'description': fields.String(required=True)
}))


product_option_type = fields.List(fields.Nested({
    'name': fields.String(required=True),
    'choices': choices_type
}))


create_ns = Namespace('wix_rest', description='Wix Rest APIs')
create_parser = reqparse.RequestParser()
create_parser.add_argument('Authorization', type=str, location='headers', help='Authorization header', required=True)
create_parser.add_argument('wix_site', type=str, help="wix site Name.", required=True)
create_parser.add_argument('name', type=str, help="name", required=True)
create_parser.add_argument('productType', type=str, help="product type", required=True)
create_parser.add_argument('price', type=float, help="product price", required=True)
create_parser.add_argument('itemCost', type=int, help="product item", required=True)
create_parser.add_argument('description', type=str, help="product id", required=True)
create_parser.add_argument('sku', type=str, help="sku", required=True)
create_parser.add_argument('visible', type=bool, help="product visible", required=True)
create_parser.add_argument('ribbon', type=str, help="ribbon", required=True)
create_parser.add_argument('brand', type=str, help="brand", required=True)
create_parser.add_argument('weight', type=float, help="product weight", required=True)
create_parser.add_argument('discount_type', type=str, help="discount_type", required=True)
create_parser.add_argument('discount_value', type=float, help="discount_value", required=True)
create_parser.add_argument('manageVariants', type=bool, help="manageVariants", required=True)
create_parser.add_argument('productOptions', type=dict, action='append', help="Product options", required=True)

@create_ns.route('/create_product')
class Product(Resource):
    @create_ns.expect(create_parser)
    def post(self):
        app_logger.info('Received request to create the product')
        app_logger.info(f'Request headers: {request.headers}')
        app_logger.info(f'Request body: {request.get_json()}')

        args = create_parser.parse_args()
        wix_site = args['wix_site']
        
        product_data = {
            "name": args['name'],
            "productType": args['productType'],
            "priceData": {"price": args['price']},
            "costAndProfitData": {"itemCost": args['itemCost']},
            "description": args['description'],
            "sku": args['sku'],
            "visible": args['visible'],
            "ribbon": args['ribbon'],
            "brand": args['brand'],
            "weight": args['weight'],
            "discount": {"type": args['discount_type'], "value": args['discount_value']},
            "manageVariants": args['manageVariants'],
            "productOptions": args['productOptions']
        }

        try:
            if not wix_site:
                return jsonify({'message': 'wix_site is required'}), 400

            app_logger.info(f'Product data to be sent: {product_data}')
            response = create_product_rest_response(wix_site, product_data)
        except Exception as e:
            exception_track = traceback.format_exc()
            app_logger.error(f'An unexpected error occurred: {e}')
            app_logger.error(f'Stack trace: {exception_track}')
            return jsonify({'message': f'Internal Server Error, {exception_track}'}), 500

        return response
