from flask import Flask
from app.users.routes import user_api

def create_app():
    app = Flask(__name__)
    print(__name__)

    app.register_blueprint(user_api)
    
    return app

