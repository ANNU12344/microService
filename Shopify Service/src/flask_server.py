from flask import Flask
from dotenv import load_dotenv
from src.Interactor.Database.sql_alchemy import setup_sqlalchemy
from src.Domain.Constant.constant import SQLALCHEMY_DATABASE_URI
from flask_swagger_ui import get_swaggerui_blueprint
from src.Interactor.Logger.custom_logger import app_logger
from flask_restx import Api, Resource, reqparse, Namespace,fields
Logger = app_logger
# Load environment variables from .env file
load_dotenv()


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SWAGGER_UI_JSONEDITOR'] = True
setup_sqlalchemy(app)


# Set up API documentation using Flask-Restx
api = Api(app, title='Shopify API', description='Set of APi to Fetch Data from Shopify stores')

# Import and register blueprints
from  src.Domain.shopify_token.server import shopify_token_bp


from  src.api.Routes.product_routes import product_ns
from  src.api.Routes.order_routes import order_ns
from  src.api.Routes.token_routes import token_ns
from  src.api.Routes.update_routes import update_ns
from  src.api.Routes.shop_info_routes import shop_info_ns
from  src.api.Routes.collection_routes import collection_ns
from  src.api.Routes.search_routes import search_ns
from  src.api.Routes.isActive_routes import isActive_ns


Logger.info("Registering blueprints")


app.register_blueprint(shopify_token_bp, url_prefix='/shopify_token')

Logger.info("Registering namespaces")


api.add_namespace(product_ns)
api.add_namespace(order_ns)
api.add_namespace(token_ns)
api.add_namespace(update_ns)
api.add_namespace(shop_info_ns)
api.add_namespace(collection_ns)
api.add_namespace(search_ns)
api.add_namespace(isActive_ns)

Logger.info("Registering swagger")

# Swagger UI configuration
SWAGGER_URL = "/swagger"
API_URL = "static/swagger.yaml"
swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': __name__}
)

app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)