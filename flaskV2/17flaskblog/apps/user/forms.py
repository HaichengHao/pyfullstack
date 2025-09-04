# @Author    : 百年
# @FileName  :forms.py
# @DateTime  :2025/9/2 12:02
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[
        DataRequired(message="请输入用户名"),
        Length(1, 20)
    ])
    password_raw = PasswordField('密码', validators=[
        DataRequired(message="请输入密码")
    ])
    phone = StringField('手机号',validators=[
        DataRequired(message='请输入手机号'),
        Length(11)
    ])
    submit = SubmitField('登录')