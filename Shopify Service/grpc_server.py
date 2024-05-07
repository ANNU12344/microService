
from concurrent import futures
import grpc
import time
import logging

from src.flask_server import app

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
from src.api.Controllers.token_controller import get_token_from_db
from src.api.grpc.services.shopify_service_pb2 import GetTokenResponse , UpdateProductResponse , UpdateCollectionResponse
from src.api.grpc.services.shopify_service_pb2_grpc import ShopifyServiceServicer, add_ShopifyServiceServicer_to_server
from src.Interactor.DTR.product_dtr import product_grpc_response
from src.Interactor.DTR.shop_dtr import shop_grpc_response
from src.Interactor.DTR.order_dtr import order_grpc_response
from src.Interactor.DTR.collection_dtr import collection_grpc_response
from src.Interactor.DTR.shop_dtr import is_active_grpc_response
from src.Interactor.DTR.search_dtr import search_grpc_response
from src.api.Controllers.product_update_controller import update_products 
from src.api.Controllers.collection_update_controller import update_collections


class ShopifyServiceHandler(ShopifyServiceServicer):
    def _with_app_context(func):
        def wrapper(self, request, context):
            with app.app_context():
                return func(self, request, context)

        return wrapper
    
    @_with_app_context
    def GetOrder(self, request, context):
        return order_grpc_response(request.shop, request.order_ids)
    
    @_with_app_context
    def GetShopInfo(self, request, context):
        return shop_grpc_response(request.shop)

    @_with_app_context
    def GetToken(self, request, context): 
        return GetTokenResponse(access_token=get_token_from_db(request.shop))
    
    @_with_app_context
    def GetProducts(self, request, context):
        print(request)
        return product_grpc_response(request.shop , request.product_ids)
    
    @_with_app_context
    def GetCollection(self, request, context):
        return collection_grpc_response(request.shop , request.collection_ids)

    @_with_app_context
    def IsActive(self, request, context):
        with app.app_context():
            response = is_active_grpc_response(request.shop)
        return response
    
    @_with_app_context
    def UpdateProduct(self, request, context):
        result = update_products(request.shop, request.id, request.title, request.description)
        return UpdateProductResponse(success=result)
    
    @_with_app_context
    def UpdateCollection(self, request, context):
        result = update_collections(request.shop, request.id, request.title, request.description)
        return UpdateCollectionResponse(success=result)
    
    @_with_app_context
    def SearchProduct(self, request, context):
        return search_grpc_response(request.shop , request.query)
    

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_ShopifyServiceServicer_to_server(ShopifyServiceHandler(), server)
    server.add_insecure_port('[::]:50051')
    print("Starting gRPC server on port 50051...")
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        logging.debug('GRPC stop')
        server.stop(0)
    #server.wait_for_termination()

if __name__ == '__main__':
    serve()
