from src.Interactor.Exception.custom_exceptions import WixAPIException , SiteNotFoundException
from src.Interactor.Logger.custom_logger import app_logger
from src.api.Controllers.product_controller import get_all_product
from flask import jsonify
def search_products(products, search_term):
    return [product for product in products if search_term.lower() in product.name.lower()]

def search_rest_response(wix_site,search_term):
    try:
        app_logger.info(f'Received REST search request for site: {wix_site}, search query: {search_term}')
        all_products = get_all_product(wix_site)

        search_results = search_products(all_products,search_term)

        products_response = [
            {"title": product.name, "description": product.description}
            for product in search_results
        ]

        response = jsonify({"products": products_response, "search_query": search_term})
        app_logger.info('Generated REST response for search')
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