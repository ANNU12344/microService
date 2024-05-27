from flask import jsonify
from src.api.Controllers.collection_controller import get_collection_by_id, get_all_collection
from src.Interactor.Exception.custom_exceptions import SiteNotFoundException,WixAPIException
from src.Interactor.Logger.custom_logger import app_logger
def collection_rest_response(wix_site,collection_id):
    try:
        if len(collection_id)==0:
            app_logger.info(f'Received request to get all collection for wix site: {wix_site}')
            collection_data = get_all_collection(wix_site)
        else:
            app_logger.info(f'Received request to get with collection {collection_id} for wix site : {wix_site}')
            collection_data = get_collection_by_id(wix_site,collection_id)

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
    
    except SiteNotFoundException as e:
        app_logger.error(f'site Not Found Exception: {e}')
        return jsonify({'error': 'site Not Found Exception'}) 
    
    except Exception as e:
        app_logger.error(f'An unexpected error occurred: {e}')
        return jsonify({'message': 'Internal Server Error'})