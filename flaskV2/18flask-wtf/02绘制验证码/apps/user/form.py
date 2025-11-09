"""
@File    :form.py
@Editor  : 百年
@Date    :2025/11/3 11:24 
"""
from flask_wtf import FlaskForm,RecaptchaField   #tips:导入recaptchaField
from wtforms import StringField, PasswordField,FileField
from wtforms.validators import DataRequired, Regexp, EqualTo, length, ValidationError
from flask_wtf.file import FileField,FileAllowed


class LoginForm(FlaskForm):
    name = StringField(label='用户名',
                       validators=[DataRequired(), length(min=6, max=12, message='输入有误,请重新输入')])
    pwd = PasswordField(label='输入密码', validators=[DataRequired(), length(min=6, max=8, message='密码长度不符合')])
    repwd = PasswordField(label='再次输入密码', validators=[DataRequired(), length(min=6, max=8),
                                                            EqualTo('pwd', message='两次密码不一致,请重新输入')])
    phone_num = StringField(label='请输入手机号码', validators=[DataRequired(), length(min=11, max=11),
                                                                Regexp(r'^1[35678]\d{9}$', message='号码有误')])
    icon = FileField(label='点击上传头像',validators=[DataRequired(),FileAllowed(['png','jpg','jpeg'],message='格式有误')])
    recaptcha = RecaptchaField(label='输入验证码') #tips:设置验证码区域



    #自定义验证
    def validate_name(self,data):
        if self.name.data[0].isdigit():
            raise ValidationError('不应该以数字开头')