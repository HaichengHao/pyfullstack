"""
@File    :model.py
@Editor  : 百年
@Date    :2025/11/28 10:14 
"""

from exts.dbhelper import db, migrate
from datetime import datetime


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(32), nullable=False)
    phone = db.Column(db.String(11))
    regi_date = db.Column(db.DateTime, default=datetime.now)
    friends = db.relationship('Friends',foreign_keys='Friends.uid' ,backref='user', lazy='dynamic')

    def __str__(self):
        return self.user_name


class Friends(db.Model):
    __tablename__ = 'friends'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uid = db.Column(db.Integer, db.ForeignKey('user.id'))
    fid = db.Column(db.Integer, db.ForeignKey('user.id'))
    create_at = db.Column(db.DateTime, default=datetime.now)
