from src.api.Controllers.order_controller import get_all_orders, get_order_by_id
from src.api.grpc.services.shopify_service_pb2 import GetOrderResponse, OrderInfo
from flask import jsonify
from src.Interactor.Logger.custom_logger import app_logger
from src.Interactor.Exception.custom_exceptions import ShopifyAPIException , StoreNotFoundException

def order_grpc_response(store, order_ids):
    try:
        if len(order_ids) == 0:
            app_logger.info(f'Received request to get all Orders for store: {store}')
            order_data = get_all_orders(store)
        else:
            app_logger.info(f'Received request to get Orders with IDs {order_ids} for store: {store}')
            order_data = get_order_by_id(store, order_ids)

        orders_info = [
            OrderInfo(id=str(order.order_number), product_id=order.order_status_url)
            for order in order_data
        ]

        response = GetOrderResponse(orders=orders_info)
        app_logger.info('Generated gRPC response for orders')
        return response
    except ShopifyAPIException as e:
        app_logger.error(f'Shopify API Exception: {e}')
        raise
    except Exception as e:
        app_logger.error(f'An unexpected error occurred: {e}')
        raise

def order_rest_response(store, order_ids):
    try:
        if len(order_ids) == 0:
            app_logger.info(f'Received request to get all Orders for store: {store}')
            order_data = get_all_orders(store)
        else:
            app_logger.info(f'Received request to get Orders with IDs {order_ids} for store: {store}')
            order_data = get_order_by_id(store, order_ids)

        orders_info = [
            {
                'title': order.order_number,
                'description': order.order_status_url
            }
            for order in order_data
        ]

        response = jsonify({"orders": orders_info})
        app_logger.info('Generated REST response for orders')
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
