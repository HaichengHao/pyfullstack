"""
@File    :model.py
@Editor  : 百年
@Date    :2025/11/17 13:13 
"""

from ..exts.dbhelper import db, migrate
from datetime import datetime


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    phone = db.Column(db.String(64), unique=True, nullable=False)
    user_icon =db.Column(db.String(150))
    regi_date = db.Column(db.DateTime, default=datetime.now())
