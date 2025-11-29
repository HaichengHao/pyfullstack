"""
@File    :model.py
@Editor  : 百年
@Date    :2025/11/26 8:38 
"""
from pygments.lexer import default

from exts.dbhelper import db
from datetime import datetime


class Userinfo(db.Model):
    __tablename__ = 'userinfo'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(15), nullable=False)
    phone = db.Column(db.String(11))
    isdelete = db.Column(db.Boolean(),default=0)
    email = db.Column(db.String(100))
    regidate = db.Column(db.DateTime, default=datetime.now)
    user_icon = db.Column(db.String(100))

    def __str__(self):
        return self.username
