"""
@File    :__init__.py.py
@Editor  : 百年
@Date    :2025/11/14 11:54 
"""
import os

from flask  import Flask
from .config import configdict
from .user.view import user_bp
import logging

def create_app():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    template_folder = os.path.join(base_dir, 'templates')
    print('--------------\n',template_folder)
    app = Flask(__name__,template_folder=template_folder)
    app.config.from_object(configdict['default'])
    app.register_blueprint(user_bp)

    #配置flask内置logger
    logger = logging.getLogger('app') #'app'是个名称,也就是设置的log是记录谁的，可以自拟
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler('flask.log')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    logger.info('这是一条信息')

    logger.warning('测试警告')

    logger.error('测试错误·')

    logger.debug('测试调试')

    return app
