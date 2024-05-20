from src.Interactor.Exception.custom_exceptions import WixAPIException , TokenNotFoundException
from src.Interactor.Logger.custom_logger import app_logger
from src.api.Controllers.product_controller import get_Product_Options_Availability
from flask import jsonify

def search_rest_response(product_id,optionType,Name,wix_site):
    try:
        app_logger.info(f'Received REST search product avaliable')
        response = get_Product_Options_Availability(product_id,optionType,Name,wix_site)
        app_logger.info('Generated REST response for search')
        return response
    except WixAPIException as e:
        app_logger.error(f'Shopify API Exception: {e}')
        return jsonify({'message': 'Shopify API Exception'})
    except TokenNotFoundException as e:
        app_logger.error(f'Store Not Found Exception: {e}')
        return jsonify({'error': 'Store Not Found Exception'})
    except Exception as e:
        app_logger.error(f'An unexpected error occurred: {e}')
        return jsonify({'message': 'Internal Server Error'})