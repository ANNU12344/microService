from flask import jsonify
from src.api.Controllers.product_controller import get_all_products, get_product_by_id
from src.api.grpc.services.shopify_service_pb2 import SearchProductResponse, ProductInfo
from src.Interactor.Logger.custom_logger import app_logger
from src.Interactor.Exception.custom_exceptions import ShopifyAPIException , StoreNotFoundException

def search_products(products, search_query):
    return [product for product in products if search_query.lower() in product.title.lower()]


def search_grpc_response(store, search_query):
    try:
        app_logger.info(f'Received gRPC search request for store: {store}, search query: {search_query}')
        all_products = get_all_products(store)

        search_results = search_products(all_products, search_query)

        products_info = [
            ProductInfo(title=product.title, description=product.body_html)
            for product in search_results
        ]

        response = SearchProductResponse(products=products_info)
        app_logger.info('Generated gRPC response for search')
        return response
    except ShopifyAPIException as e:
        app_logger.error(f'Shopify API Exception: {e}')
        raise
    except StoreNotFoundException as e:
        app_logger.error(f'Store Not Found Exception: {e}')
        raise
    except Exception as e:
        app_logger.error(f'An unexpected error occurred: {e}')
        raise


def search_rest_response(store, search_query):
    try:
        app_logger.info(f'Received REST search request for store: {store}, search query: {search_query}')
        all_products = get_all_products(store)

        search_results = search_products(all_products, search_query)

        products_response = [
            {"title": product.title, "description": product.body_html}
            for product in search_results
        ]

        response = jsonify({"products": products_response, "search_query": search_query})
        app_logger.info('Generated REST response for search')
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
    
