from flask import request, jsonify
from flask_restx import Resource, reqparse, Namespace
from src.api.Controllers.order_controller import get_order_info
from src.Interactor.Logger.custom_logger import app_logger
import traceback
order_ns = Namespace('Order Information', description='get order info with the help of order id')

order_parser = reqparse.RequestParser()
order_parser.add_argument('Authorization', type=str, location='headers', help='Authorization header', required=True)
order_parser.add_argument('order_ids', type=list, help="List of Order IDs.", required=True)


@order_ns.route('/orders')
class Order(Resource):
    @order_ns.expect(order_parser)
    def get(self):
        args = request.get_json()
        order_id = args['order_ids']
        app_logger.info(f'Recieved request to get the order info for particular order: {order_id}')
        if not isinstance(order_id):
            return jsonify({'message': 'Invalid data format. Expected a list of order_ids.'})
        
        try:
            response =  get_order_info(order_id)
        except Exception as e:
            exception_track = traceback.format_exc()
            return jsonify({'message': f'Internal Server Error , {exception_track}'})
        return response


    