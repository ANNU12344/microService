# from src.Interactor.Logger.custom_logger import app_logger
# from flask import jsonify
# from src.Interactor.Exception.custom_exceptions import BlogIdNotFoundException
# from src.api.Controllers.blog import get_all_blog , get_blog_by_id
# def blog_info_response(blog_id):
#     try:
#         if len(blog_id) == 0:
#             app_logger.info(f'Received request to get all blog post')
#             blog_object = get_all_blog()
#         else:
#             app_logger.info(f'Received request to get the particular blog info : {blog_id}')
#             products_object = get_blog_by_id(blog_id)
#             return products_object
#     except Exception as e:
#         app_logger.error(f'An unexpected error occurred: {e}')
#         raise
