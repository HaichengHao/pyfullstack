"""
@File    :view.py
@Editor  : 百年
@Date    :2025/11/16 12:26 
"""

from flask import Blueprint, jsonify
from flask_restful import Api, Resource, marshal_with, fields
from .models import User

user_bp = Blueprint('user', __name__, url_prefix='/api')
user_api = Api(user_bp)  # step1:声明一个api对象,传入的参数是蓝图对象

#tips:定制要返回的信息
resource_fields={
    'id':fields.Integer,
    'username':fields.String,
    'phone':fields.String,
    'regi_date':fields.DateTime
}

# step2:创建CBV
class Userlst(Resource):
    #tips:引用装饰器来定制返回的信息，就是上面我们定义的那个
    @marshal_with(resource_fields)
    def get(self):
        users = User.query.all()
        # user_lst=[]
        # for user in users:
        #     user_lst.append(user.__dict__)
        # return {'msg': '首页', 'num': len(users), 'user_lst': user_lst}
        # return users[0] #测试第一个
        return users
    def put(self):
        return {'message': 'put请求被调用'}

    def post(self):
        return jsonify({'message': 'post被调用'})


user_api.add_resource(Userlst, '/user')  # step3:让api对象添加CBV资源并指定好urls
