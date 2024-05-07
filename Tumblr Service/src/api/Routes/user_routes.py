from src.Interactor.Logger.custom_logger import app_logger
from flask import Blueprint, app, request, jsonify
from flask_restx import Api, Resource,Namespace,fields
# import traceback
# from src.Interactor.DTR.blog_post import blog_info_response
# from src.api.Controllers.user_method import user_info_response
# from src.Interactor.Logger.custom_logger import app_logger
user_ns= Namespace('tumblr_rest',  description='Retrieve Blog Info')

@user_ns.route('/user_info')
class BlogInfo(Resource):
    def info(self):
        app_logger.info('Received request to get the user information')
        # try:
        #     blog_info= user_info_response()
        # except Exception as e:
        #     exception_track = traceback.format_exc()
        #     app_logger.error(f'An unexpected error occurred: {e}')
        #     app_logger.error(f'An unexpected error occurred: {exception_track}')
        #     return jsonify({'message': f'Internal Server Error , {exception_track}'})

        # response = {"status": blog_info}
        
        # return jsonify(response)