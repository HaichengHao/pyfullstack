"""
@File    :__init__.py.py
@Editor  : 百年
@Date    :2025/11/9 11:23 
"""

import os
from flask import Flask
from .config import configdict
from .user.view import user_bp
from flask_wtf.csrf import CSRFProtect
def create_app():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # print('模板路径',BASE_DIR)
    template_dir = os.path.join(BASE_DIR, 'templates')
    print('模板路径', template_dir)
    app = Flask(import_name=__name__, template_folder=template_dir)
    app.config.from_object(configdict['default'])
    app.register_blueprint(user_bp)
    csrf  = CSRFProtect()
    csrf.init_app(app)
    return app