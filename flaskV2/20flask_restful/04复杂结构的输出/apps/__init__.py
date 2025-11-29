"""
@File    :__init__.py.py
@Editor  : 百年
@Date    :2025/11/28 10:00 
"""

from flask import Flask
from .api.view import api_bp
from .api.model import User, Friends
from exts.dbhelper import db, migrate
from .config import configdict


def create_app():
    app = Flask(__name__)
    app.config.from_object(configdict['default'])
    db.init_app(app)
    app.register_blueprint(api_bp)
    migrate.init_app(app, db)

    return app
