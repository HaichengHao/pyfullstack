# @Author    : 百年
# @FileName  :models.py
# @DateTime  :2025/8/27 9:04
from exts.extensions import db
from datetime import datetime

class Article(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(30),nullable=False)
    content = db.Column(db.Text,nullable=False)
    pdatetime = db.Column(db.DateTime,default=datetime.now)
    click_num = db.Column(db.Integer,default=0)
    save_num = db.Column(db.Integer,default=0)
    love_num = db.Column(db.Integer,default=0)
    user_id = db.Column(db.Integer,db.ForeignKey('uesr.id'),nullable=False) #添加外键实现一对多
    def __str__(self):
        return self.title