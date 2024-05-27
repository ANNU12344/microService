from flask import jsonify
from src.api.Controllers.product_controller import get_product_by_id, get_all_product
from src.Interactor.Exception.custom_exceptions import SiteNotFoundException,WixAPIException
from src.Interactor.Logger.custom_logger import app_logger
def product_rest_response(wix_site,product_id):
    try:
        
        if len(product_id) == 0:
            app_logger.info(f'Received request to get all Products for wix site: {wix_site}')
            products_object = get_all_product(wix_site)
        else:
            app_logger.info(f'Received request to get Product with ID {product_id} for wix site : {wix_site}')
            products_object = get_product_by_id(wix_site,product_id)


        try:
            products_response = [
                {"id" : product.id , "title": product.name, "description": product.description }
                for product in products_object
            ]
        except Exception as e:
            app_logger.error(f'An unexpected error occurred: {e}')
            app_logger.error(f'Most Likely Error is that product dont have image')
            products_response = [
                {"id" : product.id , "title": product.name, "description": product.description ,  "image_url" : "https://picsum.photos/200"}
                for product in products_object
            ]

        response = jsonify({"products": products_response})
        app_logger.info('Generated REST response for products')
        return response
    except WixAPIException as e:
        app_logger.error(f'Wix API Exception: {e}')
        return jsonify({'message': 'Wix API Exception'})
    
    except SiteNotFoundException as e:
        app_logger.error(f'Site Not Found Exception: {e}')
        return jsonify({'error': 'Site Not Found Exception'}) 
    
    except Exception as e:
        app_logger.error(f'An unexpected error occurred: {e}')
        return jsonify({'message': 'Internal Server Error'})