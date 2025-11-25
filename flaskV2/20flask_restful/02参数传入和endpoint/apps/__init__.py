"""
@File    :__init__.py.py
@Editor  : 百年
@Date    :2025/11/17 13:13 
"""
from flask import Flask
from .apis.models import User
from .config import configdict
from .apis.view import user_bp
from .exts.dbhelper import db,migrate
def create_app():
    app = Flask(__name__)
    app.config.from_object(configdict['default'])
    db.init_app(app)
    app.register_blueprint(user_bp)
    migrate.init_app(app, db)
    return app
