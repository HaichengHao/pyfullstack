"""
@File    :__init__.py.py
@Editor  : 百年
@Date    :2025/8/10 8:43 
"""
import os
from flask import Flask
from exts.extensions import db,migrate
from .config import configdict
from .user.view import user_bps
from .article.view import article_bp
from apps.user.models import User
from apps.article.models import Article
from apps.goods.view import goods_bp
from apps.goods.models import *
def create_app(configname='default'):
    app = Flask(__name__, template_folder='../templates')

    configname = configname or os.getenv('FLASK_ENV' or 'default')
    app.config.from_object(configdict[configname])

    db.init_app(app)
    app.register_blueprint(user_bps)
    app.register_blueprint(article_bp)
    app.register_blueprint(goods_bp)
    migrate.init_app(app, db)
    return app
