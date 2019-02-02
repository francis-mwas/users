from flask import Blueprint

from .user_auth import RegisterUsers

user_blueprint = Blueprint('user_auth', __name__)