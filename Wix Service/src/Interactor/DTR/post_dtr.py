from src.Interactor.Logger.custom_logger import app_logger
from src.api.Controllers.post_controller import get_all_post,get_post_by_id
from src.Interactor.Exception.custom_exceptions import TokenNotFoundException,WixAPIException
from flask import jsonify

def post_rest_response(wix_site,post_ids):
    try:
        app_logger.info(f"Starting post_rest_response)")
        if len(post_ids)==0:
            app_logger.info('Getting all posts')
            post_data=get_all_post(wix_site)
        else:
            app_logger.info(f'Getting posts by ids:{post_ids}')
            post_data = get_post_by_id(wix_site,post_ids)
        
        response = jsonify({"posts": post_data})
        app_logger.info('Post response successfully generated')
        return response
    except WixAPIException as e:
        app_logger.error(f'Wix API Exception: {e}')
        return jsonify({'message': 'Wix API Exception'})
    except TokenNotFoundException as e:
        app_logger.error(f'Token Not Found Exception: {e}')
        return jsonify({'error': 'Token Not Found Exception'}) 
    except Exception as e:
        app_logger.error(f'An unexpected error occurred: {e}')
        return jsonify({'message': 'Internal Server Error'})


