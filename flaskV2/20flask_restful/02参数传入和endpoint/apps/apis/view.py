"""
@File    :view.py
@Editor  : 百年
@Date    :2025/11/17 13:14 
"""
import os.path
import re
from ..config import Config
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename
from django.contrib.admin import action

from ..exts.dbhelper import db
from flask import Blueprint, url_for
from flask_restful import Resource, Api, marshal_with, marshal, fields, reqparse, inputs
from .models import User

user_bp = Blueprint('user', __name__)
user_api = Api(user_bp)
# tips:marshal_with是一个数据格式化和过滤工具，它就是定义了一个响应的"模板"，然后这个模板去过滤和格式化要返回给客户端的数据
#   它就像fastapi中定义响应类型差不多
resource_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'phone': fields.String,
    'regi_date': fields.DateTime
}

# tips:参数的解析
# step1:先创建一个解析器对象
parser = reqparse.RequestParser()  # tips:产生了一个解析对象
# tips:添加参数部分,注意要和前端的对应起来
# parser.add_argument('id',type=int,required=True,help='必须输入id')
parser.add_argument('username', type=str, help='用户名不能为空', location=['form'])
parser.add_argument('password', required=True, help='密码不能为空', location=['form'])
parser.add_argument('hobbies', action='append', location=['form'], dest='hobby')
parser.add_argument('usericon', type=FileStorage, location=['files'], dest='usericon')


def phone_validator(phone):
    if re.match(r'^1[3-9]\d{9}$', phone):
        return phone
    raise ValueError('手机号格式有误')


parser.add_argument('phone', type=phone_validator, location=['form'])

# important:也可以像下面这样写，不适用验证函数
# parser.add_argument('phone',type=inputs.regex(r'^1[3-9]\d{9}$'),location='json') #tips:也可以这样写


ALLOWED_EXTENSIONS = ['jpg', 'png', 'svg', 'gif', 'bmp', 'jpeg']


def check_img(file_name):
    suffix = file_name.split('.')[-1]
    if suffix in ALLOWED_EXTENSIONS:
        icon_name = secure_filename(file_name)
        return icon_name
    else:
        return False


class User_cbv(Resource):
    @marshal_with(resource_fields)
    def get(self):
        users = User.query.all()
        return users

    def put(self):
        # tips:假设我们在put的时候需要这all_user,这个路由,那么我们就将其返回
        print('endpoint的使用', url_for('user.all_user'))
        return {'msg': '成功'}

    @marshal_with(resource_fields)
    def post(self):
        # tips:解析请求数据进行验证
        parser_args = parser.parse_args()  # 拿到提交的参数，也就是上面我们定义的parser中的参数
        # 下面这些本质上就是取出post过来的值,只不过这是restful写法，理解成username=request.form.get('username')这样就会容易理解了
        username = parser_args.get('username')  # tips:或者写成parser_args['username']也是可以的
        password = parser_args.get('password')
        phone = parser_args.get('phone')
        hobbies = parser_args.get('hobby')  # 可以看看，就不往数据库中存了
        print(hobbies)

        usericon = parser_args.get('usericon')
        print(usericon)
        usericon_name = usericon.filename

        print('----------图片名称-------------',usericon_name)

        #将图片存储
        if  usericon:
            file_path = os.path.join(Config.UPLOAD_ICON_FOLDER, usericon_name)
            usericon.save(file_path)


        # secure_name = check_img(usericon_name)
        #
        # print('------------------------------------>>>>>>>>>',secure_name)


        # if secure_name:
        #     file_path = os.path.join(Config.UPLOAD_ICON_FOLDER, secure_name)
        #     usericon.save(file_path)
        #
        # print(usericon_name)

        # 创建user对象
        user = User()
        user.username = username
        user.password = password
        user.phone = phone
        user.user_icon = os.path.join('upload/icon', usericon_name).replace('\\', '/')
        db.session.add(user)
        db.session.commit()
        return user


class User_single(Resource):  # 单独只拿出一个用户的数据
    @marshal_with(resource_fields)
    def get(self, id):
        info = User.query.get_or_404(id)
        return info

    def put(self, id):
        pass

    def delete(self, id):
        pass


user_api.add_resource(User_cbv, '/user', endpoint='all_user')
user_api.add_resource(User_single, '/user/<int:id>', endpoint='singleuser')  # 传入一个用户id
