from src.Interactor.Logger.custom_logger import app_logger
from flask import request, jsonify
from flask_restx import Api, Resource, reqparse, Namespace
import traceback
# from src.Interactor.DTR.blog_post import blog_info_response

update_ns = Namespace('tumblr_rest', description='Retrieve Blog Info')
blog_parser = reqparse.RequestParser()
blog_parser.add_argument('blog_id', type=str, help="to get blog information", required=True)

@update_ns.route('/blog_info')  
class BlogInfo(Resource):
    @update_ns.expect(blog_parser)
    def post(self):  # Changed from 'info' to 'post' to match the HTTP method
        app_logger.info('Received request to get the blog info')
        app_logger.info(f'Request body: {request.get_json()}') 