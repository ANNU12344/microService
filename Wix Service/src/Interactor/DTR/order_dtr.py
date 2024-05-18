from flask import jsonify
from src.api.Controllers.order_controller import get_order_by_id
from src.Interactor.Exception.custom_exceptions import TokenNotFoundException,WixAPIException
from src.Interactor.Logger.custom_logger import app_logger
def order_rest_response(wix_site, order_id):
    try:
        app_logger.info(f'Received request to get Orders with ID {order_id} for wix site: {wix_site}')
        collection_data = get_order_by_id(wix_site,order_id)
        response = jsonify(collection_data)
        app_logger.info('Generated REST response for orders')
        return response
    except WixAPIException as e:
        app_logger.error(f'Wix API Exception: {e}')
        return jsonify({'message': 'Wix API Exception'})
    except TokenNotFoundException as e:
        app_logger.error(f'Store Not Found Exception: {e}')
        return jsonify({'error': 'Token Not Found Exception'}) 
    except Exception as e:
        app_logger.error(f'An unexpected error occurred: {e}')
        return jsonify({'message': 'Internal Server Error'})