from flask import request, jsonify
from flask_restx import Resource, reqparse, Namespace
from src.Interactor.DTR.order_dtr import order_rest_response
from src.Interactor.Logger.custom_logger import app_logger
import traceback
order_ns = Namespace('wix_rest', description='Wix Rest APIs')

order_parser = reqparse.RequestParser()
order_parser.add_argument('Authorization', type=str, location='headers', help='Authorization header', required=True)
order_parser.add_argument('wix_site', type=str, help="wix site Name", required=True)
order_parser.add_argument('order_id', type=str, help="Order ID", required=True)


@order_ns.route('/orders')
class Order(Resource):
    @order_ns.expect(order_parser)
    #I have to write decorator for authentication the requests using the wix public key
    def get(self):

        
        app_logger.info(f'Request headers: {request.headers}')
        app_logger.info(f'Request body: {request.get_json()}') 

        args = request.get_json()
        wix_site = args['wix_site'] 
        order_id = args['order_id']
        app_logger.info(f'Recieved request to get the order info for particular order: {order_id}')
        

        if not isinstance(order_id,str):
            return jsonify({'message': 'Invalid data format. Expected a list of order_ids.'})
        
        try:
            response =  order_rest_response(wix_site,order_id)
        except Exception as e:
            exception_track = traceback.format_exc()
            app_logger.error(f'An unexpected error occurred: {e}')
            app_logger.error(f'An unexpected error occurred: {exception_track}')
            return jsonify({'message': f'Internal Server Error , {exception_track}'})
        return response


    