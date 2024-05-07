from src.api.Controllers.collection_controller import get_all_collection, get_collection_by_id
from src.api.grpc.services.shopify_service_pb2 import GetCollectionResponse, CollectionInfo
from flask import jsonify
from src.Interactor.Logger.custom_logger import app_logger
from src.Interactor.Exception.custom_exceptions import ShopifyAPIException, StoreNotFoundException


def collection_grpc_response(store, collection_ids):
    try:
        app_logger.info(f'Starting collection_grpc_response for store: {store}')
        if len(collection_ids) == 0:
            app_logger.info('Getting all collections')
            collection_data = get_all_collection(store)
        else:
            app_logger.info(f'Getting collections by ID: {collection_ids}')
            collection_data = get_collection_by_id(store, collection_ids)

        collections_info = [
            CollectionInfo(
                id=str(collection.id),
                title=collection.title,
                description=collection.body_html
            )
            for collection in collection_data
        ]

        response = GetCollectionResponse(collection=collections_info)
        app_logger.info('Collection response successfully generated')
        return response
    except ShopifyAPIException as e:
        app_logger.error(f'Shopify API Exception: {e}')
        raise
    except Exception as e:
        app_logger.error(f'An unexpected error occurred: {e}')
        raise


def collection_rest_response(store, collection_ids):
    try:
        app_logger.info(f'Starting collection_rest_response for store: {store}')
        if len(collection_ids) == 0:
            app_logger.info('Getting all collections')
            collection_data = get_all_collection(store)
        else:
            app_logger.info(f'Getting collections by ID: {collection_ids}')
            collection_data = get_collection_by_id(store, collection_ids)

        collection_info = [
            {
                'id': collection.id,
                'title': collection.title,
                'description': collection.body_html
            }
            for collection in collection_data
        ]

        response = jsonify({"collections": collection_info})
        app_logger.info('Collection response successfully generated')
        return response
    except ShopifyAPIException as e:
        app_logger.error(f'Shopify API Exception: {e}')
        return jsonify({'message': 'Shopify API Exception'})
    except StoreNotFoundException as e:
        app_logger.error(f'Store Not Found Exception: {e}')
        return jsonify({'error': 'Store Not Found Exception'}) 
    except Exception as e:
        app_logger.error(f'An unexpected error occurred: {e}')
        return jsonify({'message': 'Internal Server Error'})
