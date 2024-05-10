from src.api.Controllers.collection_controller import get_collection_by_id
from flask import jsonify
from src.Interactor.Logger.custom_logger import app_logger
def collection_rest_response(collection_id,wix_site):
    try:
        app_logger.info(f'Starting collection_rest_response')
        collection_data = get_collection_by_id(collection_id,wix_site)
        response = jsonify(collection_data)
        app_logger.info('Collection response successfully generated')
        return response
    except Exception as e:
        app_logger.error(f'Wix API Exception: {e}')
        return jsonify({'message': 'Wix API Exception'})
    