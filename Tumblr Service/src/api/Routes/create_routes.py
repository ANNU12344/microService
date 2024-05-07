from src.Interactor.Logger.custom_logger import app_logger
from flask import request, jsonify
from flask_restx import Resource, reqparse, Namespace
import traceback
from src.api.Controllers.create_controller import post_blog
create_ns= Namespace('tumblr_rest',  description='posting the blog')
product_parser = reqparse.RequestParser()
product_parser.add_argument('blog_id', type=str, help="Post/ID.", required=True)
product_parser.add_argument('title', type=str, help="Title of Post.", required=True)
product_parser.add_argument('body', type=str, help="Content.", required=True)

@create_ns.route('/create')
class PostBlog(Resource):
    @create_ns.expect(product_parser)
    def post(self):
        app_logger.info('Received request to post the blog')
        app_logger.info(f'Request headers: {request.headers}')
        app_logger.info(f'Request body: {request.get_json()}') 
        args=request.get_json()
        blog_id=args['blog_id']
        title = args['title']
        content = args['body']
        if not (blog_id,title,content):
            return jsonify({'message': 'Some parameter are mising'}) ,501
        try:
            response= post_blog(blog_id,title,content)
        except Exception as e:
            exception_track = traceback.format_exc()
            app_logger.error(f'An unexpected error occurred: {e}')
            app_logger.error(f'An unexpected error occurred: {exception_track}')
            return jsonify({'message': f'Internal Server Error , {exception_track}'})

        return jsonify(response)
    

    
    



            

