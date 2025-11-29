"""
@File    :view.py
@Editor  : 百年
@Date    :2025/11/26 8:38 
"""
import email
import os.path
import re

from exts.dbhelper import db
from ..config import Config
from flask import Blueprint
from flask_restful import Api, fields, marshal_with, Resource, reqparse
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename

from .model import Userinfo

api_bp = Blueprint('api', __name__)
api = Api(api_bp)


# NeW:比如想做一个系定义的类型,因为返回的是否删除一般就只有true和false
# 我们可以自定义一个,如果为false对应未删除,否则显示已删除

# tips:下面定制一个英文转为中文显示是否删除 en to ch isdel
class e2c_isdel(fields.Raw):
    def format(self, value):
        if value:
            return '已被删除'
        else:
            return '未删除'


resp_fields = {
    'id': fields.Integer,
    'username': fields.String(attribute='username', default='匿名'),
    'phone': fields.String,
    # 'email': fields.String,
    # 'isDelete': fields.Boolean(attribute='isdelete'),
    # 'dele2c': e2c_isdel(attribute='isdelete'),  # tips:指定对应的数据库键
    # 'regidate': fields.DateTime(dt_format='rfc822')
    'uri':fields.Url(endpoint='api.singleuser', absolute=True,scheme='https'),

}

# important:我们甚至可以区分fields,结合marshalwith返回不同信息,譬如显示出icon
resp_fields_detail = {
    'id': fields.Integer,
    'username': fields.String(attribute='username', default='匿名'),
    'phone': fields.String,
    'email': fields.String,
    'isDelete': fields.Boolean(attribute='isdelete'),
    'dele2c': e2c_isdel(attribute='isdelete'),  # tips:指定对应的数据库键
    'regidate': fields.DateTime(dt_format='rfc822'),
    'usericon':fields.String(attribute='user_icon'),
}

# tips:自定义类型,如果不想用默认的str,int这种的,可以自己定义

# class String(fields.Raw):
#     """
#     Marshal a value as a string. Uses ``six.text_type`` so values will
#     be converted to :class:`unicode` in python2 and :class:`str` in
#     python3.
#     """
#     def format(self, value):
#         try:
#             return six.text_type(value)
#         except ValueError as ve:
#             raise MarshallingException(ve)


# 创建解析器
parser = reqparse.RequestParser()
parser.add_argument('username', type=str, required=True, help='用户名不能为空', location=['form'])
parser.add_argument('password', type=str, location=['form'])
parser.add_argument('email', type=str, location=['form'])
parser.add_argument('isdelete', location=['form'])
parser.add_argument('user_icon', type=FileStorage, location=['files'])


def phone_validator(phone):
    if re.match(r'^1[3-9]\d{9}$', phone):
        return phone
    raise ValueError('手机号格式有误')


parser.add_argument('phone', type=phone_validator, location=['form'])

# tips:定义图片校验
ALLOWED_EXTENSIONS = ['jpg', 'png', 'svg', 'gif', 'bmp', 'jpeg']


def check_img(file_name):
    suffix = file_name.split('.')[-1]
    if suffix in ALLOWED_EXTENSIONS:
        icon_name = secure_filename(file_name)
        return icon_name
    else:
        return False


class api_cbv(Resource):
    @marshal_with(resp_fields)
    def get(self):
        user_lst = Userinfo.query.all()
        return user_lst

    @marshal_with(resp_fields)
    def post(self):
        parser_args = parser.parse_args()
        username = parser_args.get('username')
        password = parser_args.get('password')
        phone = parser_args.get('phone')
        usericon = parser_args.get('user_icon')
        print(usericon)
        usericon_name = usericon.filename
        if usericon:
            file_path = os.path.join(Config.UPLOAD_ICON_FOLDER, usericon_name)
            usericon.save(file_path)
        else:
            pass
        # tips:创建Userinfo对象
        user = Userinfo()
        user.username = username
        user.password = password
        user.phone = phone
        user.user_icon = os.path.join('upload/icon', usericon_name).replace('\\', '/')
        db.session.add(user)
        db.session.commit()
        return user


class User_single(Resource):
    @marshal_with(resp_fields_detail)
    def get(self, id):
        info = Userinfo.query.get(id)
        return info


api.add_resource(api_cbv, '/user', endpoint='all_user')
api.add_resource(User_single, '/user/<int:id>', endpoint='singleuser')
