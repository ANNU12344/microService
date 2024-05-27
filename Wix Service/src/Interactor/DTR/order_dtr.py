from flask import jsonify
from src.api.Controllers.order_controller import get_order_by_id,get_all_order
from src.Interactor.Exception.custom_exceptions import SiteNotFoundException,WixAPIException
from src.Interactor.Logger.custom_logger import app_logger
def order_rest_response(wix_site, order_id):
    try:
        if len(order_id)==0:
            app_logger.info(f'Received request to get all order for wix site: {wix_site}')
            order_data = get_all_order(wix_site)
        else:
            app_logger.info(f'Received request to get Product with ID {order_id} for wix site : {wix_site}')
            order_data = get_order_by_id(wix_site,order_id)

        order_info = [
            {
                'id': order.id
            }
            for order in order_data
        ]

        response = jsonify({"Order": order_info})
        app_logger.info('Order response successfully generated')
        return response
    except WixAPIException as e:
        app_logger.error(f'Wix API Exception: {e}')
        return jsonify({'message': 'Wix API Exception'})
    except SiteNotFoundException as e:
        app_logger.error(f'Site Not Found Exception: {e}')
        return jsonify({'error': 'Site Not Found Exception'}) 
    except Exception as e:
        app_logger.error(f'An unexpected error occurred: {e}')
        return jsonify({'message': 'Internal Server Error'})