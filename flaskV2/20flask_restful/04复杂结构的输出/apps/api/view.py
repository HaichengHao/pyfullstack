"""
@File    :view.py
@Editor  : 百年
@Date    :2025/11/28 10:02 
"""
from flask_restful import Api, Resource, fields, marshal_with, reqparse, marshal
from flask import Blueprint

from exts.dbhelper import db
from .model import User, Friends
import re

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

resp_field = {
    'name': fields.String(attribute='user_name'),
    'phone': fields.String,
}
demo_field = {
    'regi_date': fields.String,
    'phone': fields.String,
    'user_name': fields.String

}

friend_set={
    '好友id':fields.Integer(attribute='id'),
    '好友名':fields.String(attribute='user_name'),
    '好友手机号':fields.String(attribute='phone'),
}

# 创建解析器处理post请求
parser = reqparse.RequestParser()
parser.add_argument('user_name', type=str, required=True, help='用户名不能为空', location=['form'])


def phone_validator(phone):
    if re.match(r'^1[3-9]\d{9}$', phone):
        return phone
    else:
        raise ValueError('手机号格式有误')


parser.add_argument('phone', type=phone_validator, location=['form'])


class ApiCBV(Resource):
    def get(self):
        users = User.query.all()
        return marshal(users, demo_field)

    @marshal_with(resp_field)
    def post(self):
        parser_args = parser.parse_args()
        username = parser_args.get('user_name')
        phone = parser_args.get('phone')

        user = User()
        user.user_name = username
        user.phone = phone
        db.session.add(user)
        db.session.commit()
        return user


# class FriendCBV(Resource):
#     # tips:获取用户的朋友信息,传入一个用户id,获取该id的所有好友的id
#     def get(self, uid):
#         # tips:先定位到此人，利用.get进行主键查询
#         usr = User.query.get(uid)
#         # tips:拿到指定uid,去Friends表中拿
#         uids_friends = Friends.query.filter(Friends.uid == uid).all()
#         friends_lst = []
#         for friend in uids_friends:
#             # tips 然后拿到此uid的所有user对象f
#             f = User.query.get(friend.fid)
#             # fid = f.id  # 拿到f对象的id
#             # fname = f.user_name  # tips:然后拿到其对应的user_name键
#             # f_info_set = {
#             #     '好友id': fid,
#             #     '好友名': fname
#             # }
#             # friends_lst.append(f_info_set)
#             friends_lst.append(f)
#         uid_data = {
#             'username': usr.user_name,
#             'friends_num': len(uids_friends),
#             # 'friends_lst': friends_lst
#             'friends_lst': marshal(friends_lst,friend_set)
#         }
#         return uid_data
#


#  important :优化查询速度
# class FriendCBV(Resource):
#     # tips:获取用户的朋友信息,传入一个用户id,获取该id的所有好友的id
#     def get(self, uid):
#         # tips:先定位到此人，利用.get进行主键查询
#         usr = User.query.get(uid)
#         if not usr:
#             return {'error':'该用户不存在'},404
#
#         #NeW:优化查询速度,这样只需要两次查询而不是上面的n+1次查询
#         #step1: 获取所有好友的fid列表
#         friend_ids=[f.fid  for f in Friends.query.filter(Friends.uid == uid).all()]
#
#         #step2:  一次性查询出所有好友User对象
#         friends=User.query.filter(User.id.in_(friend_ids)).all()
#
#
#         uid_data = {
#             'username': usr.user_name,
#             'friends_num': len(friends),
#             # 'friends_lst': friends_lst
#             'friends_lst': marshal(friends,friend_set)
#         }
#         return uid_data

#NeW :使用marshal_with()与fields.Nested嵌套
user_friend_fields={
    'username':fields.String,
    'friends_num':fields.Integer,
    'friends_lst':fields.List(fields.Nested(friend_set)),
}
class FriendCBV(Resource):
    @marshal_with(user_friend_fields)
    # tips:获取用户的朋友信息,传入一个用户id,获取该id的所有好友的id
    def get(self, uid):
        # tips:先定位到此人，利用.get进行主键查询
        usr = User.query.get(uid)
        if not usr:
            return {'error':'该用户不存在'},404

        #NeW:优化查询速度,这样只需要两次查询而不是上面的n+1次查询
        #step1: 获取所有好友的fid列表
        friend_ids=[f.fid  for f in Friends.query.filter(Friends.uid == uid).all()]

        #step2:  一次性查询出所有好友User对象实例
        friends=User.query.filter(User.id.in_(friend_ids)).all()


        uid_data = {
            'username': usr.user_name,
            'friends_num': len(friends),
            'friends_lst': friends
        }
        return uid_data

api.add_resource(ApiCBV, '/user', endpoint='user')
api.add_resource(FriendCBV, '/friends/<int:uid>', endpoint='friends')
