"""
@File    :__init__.py.py
@Editor  : 百年
@Date    :2025/11/2 21:28 
"""
import os

from flask import Flask
from .user.view import user_bp
from .config import configdict
def create_app():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # print('模板路径',BASE_DIR)
    template_dir = os.path.join(BASE_DIR, 'templates')
    print('模板路径',template_dir)
    app = Flask(import_name=__name__, template_folder=template_dir)
    app.config.from_object(configdict['default'])
    app.register_blueprint(user_bp)

    # app.secret_key='igufa128970,.iuasd67'
    return app
