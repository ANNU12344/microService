from flask import jsonify
from src.api.Controllers.product_controller import get_product_by_id
from src.Interactor.Exception.custom_exceptions import TokenNotFoundException,WixAPIException
from src.Interactor.Logger.custom_logger import app_logger
def product_rest_response(wix_site,product_id):
    
    try:
        app_logger.info(f'Received request to get Product with ID {product_id} for wix site: {wix_site}')
        product_data = get_product_by_id(wix_site,product_id)
        response = jsonify(product_data)
        app_logger.info('Product response successfully generated')
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