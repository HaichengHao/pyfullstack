"""
@File    :__init__.py
@Editor  : 百年
@Date    :2025/11/16 12:26 
"""

from flask import Flask
from .config import configdict
from exts.dbhelper import db,migrate
from .api.view import user_bp
from .api.models import User
def create_app():
    app = Flask(__name__)
    app.config.from_object(configdict['default'])
    db.init_app(app)
    app.register_blueprint(user_bp)
    migrate.init_app(app, db)

    return app
