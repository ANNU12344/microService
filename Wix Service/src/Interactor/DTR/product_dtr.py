from src.api.Controllers.product_controller import get_product_by_id
from flask import jsonify
from src.Interactor.Logger.custom_logger import app_logger
def product_rest_response(product_id):
    try:
        app_logger.info(f'Starting collection_rest_response')
        app_logger.info(f'Getting product by ID: {product_id}')
        collection_data = get_product_by_id(product_id)
        app_logger.info("Successfully response generated")
        response = jsonify(collection_data)
        app_logger.info('Product response successfully generated')
        return response
    except Exception as e:
        app_logger.error(f'Wix API Exception: {e}')
        return jsonify({'message': 'Wix API Exception'})