""" Global Imports """
from flask import Flask
from flask_restful import Api
from instance.config import app_config

""" Blueprints """
from .auth import user_blueprint as users_blp


""" Module imports """
from .auth.user_auth import RegisterUsers, Login




""" creating an application instance """
def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
   
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    """ Registering application blueprint """
    users = Api(users_blp)
    app.register_blueprint(users_blp, url_prefix='/api/v1/auth')

   

    """ creating endpoints """
    users.add_resource(RegisterUsers, '/signup')
        
    users.add_resource(Login, '/login')

    

   
   
    return app


