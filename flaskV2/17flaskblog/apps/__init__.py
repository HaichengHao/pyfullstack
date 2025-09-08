"""
@File    :__init__.py.py
@Editor  : 百年
@Date    :2025/8/10 8:43 
"""
import os
from flask import Flask, request, session, redirect, jsonify
from exts.extensions import db, migrate
from .config import configdict
from .user.view import user_bps
from .article.view import article_bp
from apps.user.models import User
from apps.article.models import Article
from apps.goods.view import goods_bp
from apps.goods.models import *
def create_app(configname='default'):
    # app = Flask(__name__, template_folder='templates')
    basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    template_dir = os.path.join(basedir, 'templates')
    static_dir = os.path.join(basedir,'static')

    app = Flask(__name__, template_folder=template_dir,static_folder=static_dir)
    # app.secret_key = ';ouahsef;euahiuhiluh'
    configname = configname or os.getenv('FLASK_ENV' or 'default')
    app.config.from_object(configdict[configname])

    db.init_app(app)
    app.register_blueprint(user_bps)
    app.register_blueprint(article_bp)
    app.register_blueprint(goods_bp)

    @app.before_request
    def auth():
        # important:新操作,解决样式问题,新的白名单
        if request.path.startswith('/static/') or request.path == '/favicon.ico':
            return
        # important:设置白名单,不然用户会卡循环登录最后报错,白名单里放的是无需登录就能访问的页面
        if request.path in ["/login",'/login_verifycode', '/register','/checkphone']:
            return

        print('请求前操作')
        result = session.get('uname')
        print(result)
        # if result:  # 如果正确则返回页面
        #     return render_template('index.html', msg=result)  important:这样做会产生逻辑循环,导致index中插入数据不会返回结果

        if not result:
            # ✅ 区分 AJAX 请求
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return jsonify(code=401, msg='未登录'), 401
            return redirect('/login')
    migrate.init_app(app, db)
    return app
