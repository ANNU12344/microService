from src.api.Controllers.product_controller import get_all_products, get_product_by_id
from src.api.grpc.services.shopify_service_pb2 import GetProductsResponse, ProductInfo
from src.Interactor.Logger.custom_logger import app_logger
from flask import jsonify
from src.Interactor.Exception.custom_exceptions import ShopifyAPIException, StoreNotFoundException

def product_grpc_response(store_name, product_ids):
    try:
        if len(product_ids) == 0:
            app_logger.info(f'Received request to get all Products for store: {store_name}')
            products_object = get_all_products(store_name)
        else:
            app_logger.info(f'Received request to get Products with IDs {product_ids} for store: {store_name}')
            products_object = get_product_by_id(store_name, product_ids)

        products_info = [
            ProductInfo(title=product.title, description=product.body_html)
            for product in products_object
        ]

        response = GetProductsResponse(products=products_info)
        app_logger.info('Generated gRPC response for products')
        return response
    except ShopifyAPIException as e:
        app_logger.error(f'Shopify API Exception: {e}')
        raise
    except Exception as e:
        app_logger.error(f'An unexpected error occurred: {e}')
        raise

def product_rest_response(store_name, product_ids):
    try:
        if len(product_ids) == 0:
            app_logger.info(f'Received request to get all Products for store: {store_name}')
            products_object = get_all_products(store_name)
        else:
            app_logger.info(f'Received request to get Products with IDs {product_ids} for store: {store_name}')
            products_object = get_product_by_id(store_name, product_ids)

        try:
            products_response = [
                {"id" : product.id , "title": product.title, "description": product.body_html , "image_url" : product.image['src']}
                for product in products_object
            ]
        except Exception as e:
            app_logger.error(f'An unexpected error occurred: {e}')
            app_logger.error(f'Most Likely Error is that product dont have image')
            products_response = [
                {"id" : product.id , "title": product.title, "description": product.body_html ,  "image_url" : "https://picsum.photos/200"}
                for product in products_object
            ]

        response = jsonify({"products": products_response})
        app_logger.info('Generated REST response for products')
        return response
    except ShopifyAPIException as e:
        app_logger.error(f'Shopify API Exception: {e}')
        return jsonify({'error': 'Shopify API Exception'})
    except StoreNotFoundException as e:
        app_logger.error(f'Store Not Found Exception: {e}')
        return jsonify({'error': 'Store Not Found Exception'}) 
    except Exception as e:
        app_logger.error(f'An unexpected error occurred: {e}')
        return jsonify({'error': 'Internal Server Error'})
