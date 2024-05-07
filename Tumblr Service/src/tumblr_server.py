from flask import Flask
from dotenv import load_dotenv
from src.Domain.Constant.constant import SQLALCHEMY_DATABASE_URI
from src.Interactor.Logger.custom_logger import app_logger
from src.api.Routes.create_routes import create_ns
from src.api.Routes.search_routes import search_ns
from src.api.Routes.user_routes import user_ns
from src.api.Routes.update_routes import update_ns
from flask_restx import Api
Logger = app_logger
load_dotenv()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SWAGGER_UI_JSONEDITOR'] = True
api = Api(app, title='Tumblr API', description='Set of API to post the blog on Tumblr')
api.add_namespace(create_ns,path='/create')
api.add_namespace(update_ns,path='/update')
api.add_namespace(search_ns,path='/search')
api.add_namespace(user_ns,path='/user')
