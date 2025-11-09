"""
@File    :__init__.py
@Editor  : 百年
@Date    :2025/10/29 10:44 
"""
import os.path
from flask import Flask
from .user.view import user_bps
from flask_wtf.csrf import CSRFProtect
from .config import configdict
probj_folder = os.path.dirname(os.path.dirname(__file__))


def create_app(config_name='default'):
    app = Flask(__name__, template_folder=os.path.join(probj_folder, 'templates'))
    app.config.from_object(configdict[config_name])
    # 开启csrf全局保护
    csrf = CSRFProtect()
    csrf.init_app(app)

    app.secret_key = 'jgabkd671;.as1sdh1278uiophsh'  # 要使用csrf保护的话需要设置secret_key
    app.register_blueprint(user_bps)

    return app
