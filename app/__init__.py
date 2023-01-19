from flask import Flask
from app.users.routes import user_api
from app.items.routes import item_api
from app.sales.routes import sale_api


def create_app():
    app = Flask(__name__)
    print(__name__)

    app.register_blueprint(user_api)
    app.register_blueprint(item_api)
    app.register_blueprint(sale_api)
    
    return app

