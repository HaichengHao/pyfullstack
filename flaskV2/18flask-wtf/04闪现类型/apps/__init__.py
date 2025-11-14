"""
@File    :__init__.py.py
@Editor  : 百年
@Date    :2025/11/14 11:54 
"""
import os

from flask  import Flask
from .config import configdict
from .user.view import user_bp

def create_app():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    template_folder = os.path.join(base_dir, 'templates')
    print('--------------\n',template_folder)
    app = Flask(__name__,template_folder=template_folder)
    app.config.from_object(configdict['default'])
    app.register_blueprint(user_bp)


    return app
