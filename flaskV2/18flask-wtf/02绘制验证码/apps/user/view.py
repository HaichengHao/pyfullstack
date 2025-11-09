"""
@File    :views.py
@Editor  : 百年
@Date    :2025/11/2 21:29 
"""
import os.path

from ..config import Config
from flask import render_template, Blueprint,request
from .form import LoginForm

user_bp = Blueprint('user', __name__, url_prefix='/user')


@user_bp.route('/index', endpoint='index')
def index_rt():
    return render_template('user/index.html')


# @user_bp.route('/login', endpoint="login",methods=['POST','GET'])
# def login_rt():
#     login_form = LoginForm()
#     if login_form.validate_on_submit():
#         name = login_form.name.data
#         pwd = login_form.pwd.data
#         repwd = login_form.repwd.data
#         icon = login_form.icon.data
#         print(icon.filename)
#         save_path = os.path.join(Config.UPLOAD_ICON_FOLDER, icon.filename)
#         login_form.icon.data.save(save_path)
#
#     return render_template('user/login.html',login_form=login_form)


@user_bp.route('/login', methods=['GET', 'POST'], endpoint="login")
def login_rt():
    login_form = LoginForm()
    print("Form errors:", login_form.errors)  # ← 加这行
    if login_form.validate_on_submit():
        print("✅ 表单验证通过！")
        # ... 保存文件
    else:
        if request.method == 'POST':
            print("❌ POST 提交但验证失败:", login_form.errors)
    return render_template('user/login.html', login_form=login_form)