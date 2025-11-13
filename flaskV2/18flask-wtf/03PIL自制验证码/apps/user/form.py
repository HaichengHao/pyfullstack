"""
@File    :form.py
@Editor  : 百年
@Date    :2025/11/9 12:00 
"""
from flask_wtf import FlaskForm
from wtforms import StringField, FileField, PasswordField
from wtforms.validators import DataRequired, length, Regexp, EqualTo, ValidationError
from flask_wtf.file import FileAllowed
from flask import session


class LoginForm(FlaskForm):
    name = StringField(label='用户名', validators=[DataRequired(), length(min=4, max=12, message='长度限定为4-12')])
    pwd = PasswordField(label='密码', validators=[DataRequired(), length(min=6, max=16, message='6-16位，请重新输入')])
    repwd = PasswordField(label='再次输入',
                          validators=[DataRequired(), EqualTo('pwd', message='两次密码不一致请重新输入')])
    icon = FileField(label='头像',
                     validators=[DataRequired(), FileAllowed(['png', 'jpg', 'jpeg'], message='只允许png,jpg,jpeg格式')])
    phone_num = StringField(label='手机号', validators=[DataRequired(), length(min=11, max=11),
                                                        Regexp(r'^1[356789]\d{9}$', message='格式有误')])
    captcha = StringField(label='验证码', validators=[DataRequired(), length(min=6, max=6)])

    def validate_captcha(self, data):
        input_code = data.data  # 相当于self.captcha.data
        if input_code.lower() != session.get('vc_code').lower():
            raise ValidationError("验证码错误")
