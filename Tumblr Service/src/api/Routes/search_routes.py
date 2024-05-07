from src.Interactor.Logger.custom_logger import app_logger
from flask import request, jsonify
from flask_restx import Api, Resource, reqparse, Namespace
import traceback
from src.api.Controllers.search_controller import search_blog
# from src.Interactor.DTR.blog_post import blog_info_response

search_ns = Namespace('tumblr_rest', description='Retrieve Blog Info')
blog_parser = reqparse.RequestParser()
blog_parser.add_argument('blog_id', type=str, help="to get blog information", required=True)
blog_parser.add_argument('post_id', type=str, help="to get blog information", required=True)
@search_ns.route('/blog_info')  
class BlogInfo(Resource):
    @search_ns.expect(blog_parser)
    def post(self):  # Changed from 'info' to 'post' to match the HTTP method
        app_logger.info('Received request to get the blog info')
        app_logger.info(f'Request body: {request.get_json()}') 
        args = blog_parser.parse_args()  # Correct way to parse arguments
        blog_id = args['blog_id']
        post_id=args['post_id']
        try:
            blog_info = search_blog(blog_id,post_id)
        except Exception as e:
            exception_track = traceback.format_exc()
            app_logger.error(f'An unexpected error occurred: {e}')
            app_logger.error(f'An unexpected error occurred: {exception_track}')
            return jsonify({'message': f'Internal Server Error, {exception_track}'}), 500

        response = {"status": blog_info}
        return jsonify(response)
