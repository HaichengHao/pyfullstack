"""
@File    :__init__.py.py
@Editor  : 百年
@Date    :2025/11/26 8:37 
"""
from flask import Flask
from .apis.model import Userinfo
from .apis.view import api_bp
from .config import configdict
from exts.dbhelper import db,migrate


def create_app():
    app = Flask(__name__)
    app.config.from_object(configdict['default'])
    db.init_app(app)
    app.register_blueprint(api_bp)
    migrate.init_app(app, db)
    return app
