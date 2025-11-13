"""
@File    :view.py
@Editor  : 百年
@Date    :2025/11/9 11:57 
"""
from io import BytesIO

from flask import  Blueprint, request, render_template,make_response,session
from .form import LoginForm
from .captchagen  import generate_captcha
user_bp = Blueprint('user', import_name=__name__, url_prefix='/user')


@user_bp.route('/login', endpoint='login', methods=['GET', 'POST'])
def login_rt():
    # 创建表单
    login_form = LoginForm()
    if login_form.validate_on_submit():
        return make_response('success')

    return render_template('user/login.html', login_form=login_form)

@user_bp.route('/captcha', endpoint='captcha', methods=['GET', 'POST'])
def captcha_rt():
    vc_code,captcha = generate_captcha(length=6)

    #保存到redis或session中(最好放到redis中,因为它可以设置失效时间且更安全)
    session['vc_code'] = vc_code


    #将验证码转为二进制
    buffer = BytesIO() #构建缓冲区
    captcha.save(buffer,"JPEG") #将验证码存入缓冲区当中
    buffer_bytes = buffer.getvalue() #读出内容
    resp = make_response(buffer_bytes)
    resp.headers['Content-Type'] = 'image/jpeg' #important:必须设置!!否则会格式不被识别将会出错
    return resp


#tips:实现form与bootstrap结合的路由
@user_bp.route('/signup',endpoint='signup', methods=['GET', 'POST'])

def signup_rt():
    #创建表单
    signup_form=LoginForm()
    if signup_form.validate_on_submit():
        return make_response('success')
    return render_template('user/signup.html', signup_form=signup_form)