from urllib import response
from src.api.Controllers.shop_data_controller import get_shop_data
from src.api.Controllers.token_controller import token_exist
from src.api.grpc.services.shopify_service_pb2 import GetShopInfoResponse, IsActiveResponse
from src.Interactor.Logger.custom_logger import app_logger
from flask import jsonify
from src.Interactor.Exception.custom_exceptions import ShopifyAPIException , StoreNotFoundException


def shop_grpc_response(store):
    try:
        app_logger.info(f'Received gRPC request for shop info for store: {store}')
        Shop_data = get_shop_data(store)
        response = GetShopInfoResponse(
            name=Shop_data.name,
            email=Shop_data.email,
            country=Shop_data.country,
            currency=Shop_data.currency,
            timezone=Shop_data.timezone,
            phone=Shop_data.phone,
            city=Shop_data.city
        )
        app_logger.info('Generated gRPC response for shop info')
        return response
    except ShopifyAPIException as e:
        app_logger.error(f'Shopify API Exception: {e}')
        raise
    except Exception as e:
        app_logger.error(f'An unexpected error occurred: {e}')
        raise


def shop_rest_response(store):
    try:
        app_logger.info(f'Received REST request for shop info for store: {store}')
        Shop_data = get_shop_data(store)
        response = {
            'id' : Shop_data.id,
            'name': Shop_data.name,
            'email': Shop_data.email,
            'country': Shop_data.country,
            'currency': Shop_data.currency,
            'timezone': Shop_data.timezone,
            'phone': Shop_data.phone,
            'city': Shop_data.city
        }
        app_logger.info('Generated REST response for shop info')
        return jsonify(response)
    except ShopifyAPIException as e:
        app_logger.error(f'Shopify API Exception: {e}')
        return jsonify({'message': 'Shopify API Exception'})
    except StoreNotFoundException as e:
        app_logger.error(f'Store Not Found Exception: {e}')
        return jsonify({'error': 'Store Not Found Exception'})
    except Exception as e:
        app_logger.error(f'An unexpected error occurred: {e}')
        return jsonify({'message': 'Internal Server Error'})


def is_active_grpc_response(store):
    try:
        app_logger.info(f'Received gRPC request for checking store activity for store: {store}')
        response = token_exist(store)
        app_logger.info(f'Shopify store is {"active" if response else "inactive"}')
        return IsActiveResponse(
            is_active=response,
            description="Shopify store is active"
        )
    except Exception as e:
        app_logger.error(f'An unexpected error occurred: {e}')
        raise
    

def is_active_rest_response(store):
    try:
        app_logger.info(f'Received REST request for checking store activity for store: {store}')
        response = token_exist(store)
        app_logger.info(f'Shopify store is {"active" if response else "inactive"}')
        return jsonify({"is_active": response})
    except Exception as e:
        app_logger.error(f'An unexpected error occurred: {e}')
        return jsonify({'message': 'Internal Server Error'})
