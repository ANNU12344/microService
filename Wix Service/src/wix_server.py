from flask import Flask
from src.Interactor.Database.sql_alchemy import setup_sqlalchemy
from src.Domain.wix_token.server import wix_token_bp
from src.api.Routes.order_routes import order_ns
from src.api.Routes.product_routes import product_ns
from src.api.Routes.update_routes import update_ns
from src.api.Routes.collection_routes import collection_ns 
from src.api.Routes.search_routes import search_ns 
from src.api.Routes.token_routes import token_ns
from src.api.Routes.post_routes import post_ns
from src.api.Routes.delete_routes import delete_ns
from src.api.Routes.create_product_routes  import create_ns
from src.api.Routes.create_collection_routes import create_collection_ns
from src.Domain.Constant.constant import SQLALCHEMY_DATABASE_URI
from flask_restx import Api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SWAGGER_UI_JSONEDITOR'] = True
setup_sqlalchemy(app)


app.register_blueprint(wix_token_bp, url_prefix='/wix_token')
api = Api(app)
api.add_namespace(order_ns) 
api.add_namespace(product_ns) 
api.add_namespace(update_ns) 
api.add_namespace(collection_ns) 
api.add_namespace(search_ns ) 
api.add_namespace(token_ns) 
api.add_namespace(post_ns)  
api.add_namespace(delete_ns)
api.add_namespace(create_ns)
api.add_namespace(create_collection_ns)




