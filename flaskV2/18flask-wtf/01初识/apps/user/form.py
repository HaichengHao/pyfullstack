"""
@File    :form.py
@Editor  : 百年
@Date    :2025/10/29 10:49 
"""
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, length, ValidationError, EqualTo, Regexp
import re


class UserForm(FlaskForm):
    name = StringField(label='用户名', validators=[DataRequired(), length(min=4, max=12, message="用户名最少4位，最多12位")])
    pwd = PasswordField(label='密码', validators=[DataRequired(), length(min=6, max=12, message="密码最少为6位,最多12位")])
    confirm_pwd = PasswordField(label='确认密码',
                                validators=[DataRequired(), length(min=6, max=12, message="密码最少为6位,最多12位"),
                                            EqualTo('pwd', message="两次密码不一致")])

    phone_num = StringField(label='输入手机号', validators=[DataRequired(), length(min=11, max=11, message='格式有误,请检查'),
                                                       Regexp(r'^1[35678]\d{9}$', message='号码格式错误')])

    # 利用文件上传功能

    icon = FileField(label='选择头像', validators=[FileRequired(), FileAllowed(['jpg','png','gif'],message='格式有误,请重选')])



    # 自定义校验

    def validate_name(self, data):
        if self.name.data[0].isdigit():  # 如果名称以数字开头则拒绝
            print('名字是以数字开头')
            print(self.name.data)  # 这样可以直接拿到输入的name的值
            print('data是------------------', data)  # tips:这样拿到的是一个表单
            print(type(data))
            # tips:如果是以数字开头那么就要抛出异常了
            raise ValidationError('用户名不能以数字开头')

        # 名字是以数字开头
        # 112233
        # data是------------------ <input id="name" maxlength="12" minlength="4" name="name" required type="text" value="112233">
        # 可以看到data其实就是生成的表单
        # <class 'wtforms.fields.simple.StringField'>  tips:可以看到其类型是一个wtform表单字符域

        # def validate_confirm_pwd(self, data):
        #     if self.confirm_pwd.errors:
        #         print(self.confirm_pwd.data)
        #         print(self.confirm_pwd)
        #         raise ValidationError('两次密码不一致')

        # tips:单独定义手机号码验证因为默认stringfiled里面没有关于手机号码验证用的子类
        # def validate_phone_num(self, data):
        #     phone = data.data
        #     # # pth = '1[35678]\d{9}$'  # 这样的正则表达式的意思就是以1开头,然后3,5,6,7,8作为第二个数字的备选,后面跟上9位数字
        #     # if not re.search(r'^1[35678]\d{9}$',phone):
        #     #     res = re.search(r'^1[35678]\d{9}$',phone)
        #     #     print(res)
        #     #     raise ValidationError('号码格式错误')
        #
        #     res = re.search(r'^1[35678]\d{9}$', phone)
        #     if res == None: #判断,如果不匹配那么返回的就是none，那就甩出报错
        #         raise ValidationError('号码格式错误')

        '''注意
        # None <--如果没匹配到指定的pattern的话返回的是None
        # 注意，match在匹配的时候，是从字符串的开头匹配的
        # 例如我们写的匹配规则是 \d+ 而经过match之后就变成了 ^\d+
        # 即匹配规则变成了字符串开头，可我们的字符串开头并不是数字'''

        # tips:这样我们的思路就明确了,如果result为None,那就说明输入的格式不正确，我们这时候可以甩出错误提示
