from flask import jsonify
from src.api.Controllers.collection_controller import get_collection_by_id
from src.Interactor.Exception.custom_exceptions import TokenNotFoundException,WixAPIException
from src.Interactor.Logger.custom_logger import app_logger
def collection_rest_response(wix_site,collection_id):
    try:
        app_logger.info(f'Received request to get Collection with ID {collection_id} for wix site: {wix_site}')
        collection_data = get_collection_by_id(wix_site,collection_id)
        app_logger.info(f'collection_data -> {collection_data}')
        collection_info = [
            {
                'id': collection.id,
                'title': collection.name,
                'description': collection.description
            }
            for collection in collection_data
        ]

        response = jsonify({"collections": collection_info})
        app_logger.info('Collection response successfully generated')
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