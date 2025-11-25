"""
@File    :view.py
@Editor  : 百年
@Date    :2025/11/14 12:07 
"""
from django.http import HttpResponse
from flask import Blueprint, request, render_template, flash,redirect,url_for,current_app

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/',endpoint='index')
def index_rt():
    return render_template('user/index.html')


@user_bp.route('/login', methods=['GET', 'POST'],endpoint='login')
def login_rt():
    if request.method == 'POST':

        name = request.form.get('username')
        pwd = request.form.get('pwd')
        if name == 'admin':
            flash('非常恭喜',category='error')
            flash(name,category='info')
            flash('验证成功!!',category='warning')  # tips:相当于也是对页面传出一个消息,只不过是不通过render_template了
            # return render_template('user/index.html')
            return redirect(url_for('user.index'))
        else:
            current_app.logger.debug('出错咯！！')
            current_app.logger.warning('这是一个警告')
            current_app.logger.error('这是一个错误')
    return render_template('user/login.html')