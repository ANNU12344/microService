from flask import request, jsonify
from flask_restx import Resource, reqparse, Namespace
from src.api.Controllers.order_controller import get_order_info
from src.Interactor.Logger.custom_logger import app_logger
import traceback
order_ns = Namespace('Order Information', description='get order info with the help of order id')

order_parser = reqparse.RequestParser()
order_parser.add_argument('Authorization', type=str, location='headers', help='Authorization header', required=True)
order_parser.add_argument('wix_site', type=str, help="wix site Name", required=True)
order_parser.add_argument('order_id', type=str, help="Order ID", required=True)


@order_ns.route('/orders')
class Order(Resource):
    @order_ns.expect(order_parser)
    def get(self):

        app_logger.info(f'Recieved request to get the order info for particular order: {order_id}')
        app_logger.info(f'Request headers: {request.headers}')
        app_logger.info(f'Request body: {request.get_json()}') 

        args = request.get_json()
        order_id = args['order_ids']
        wix_site = args['wix_site'] 

        if not isinstance(order_id,str):
            return jsonify({'message': 'Invalid data format. Expected a list of order_ids.'})
        
        try:
            response =  get_order_info(order_id,wix_site)
        except Exception as e:
            exception_track = traceback.format_exc()
            app_logger.error(f'An unexpected error occurred: {e}')
            app_logger.error(f'An unexpected error occurred: {exception_track}')
            return jsonify({'message': f'Internal Server Error , {exception_track}'})
        return response


    