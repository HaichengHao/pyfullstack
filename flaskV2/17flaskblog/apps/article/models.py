# @Author    : 百年
# @FileName  :models.py
# @DateTime  :2025/8/27 9:04
from exts.extensions import db
from datetime import datetime


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(30), nullable=False)
    content = db.Column(db.Text, nullable=False)
    pdatetime = db.Column(db.DateTime, default=datetime.now)
    click_num = db.Column(db.Integer, default=0)
    save_num = db.Column(db.Integer, default=0)
    love_num = db.Column(db.Integer, default=0)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # 添加外键实现一对多
    type_id = db.Column(db.Integer,db.ForeignKey('article_type.id'),nullable=True)
    comment = db.relationship('Comment', backref='article')

    def __str__(self):
        return self.title


class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    comment = db.Column(db.String(255), nullable=False)
    # tips:与用户表的主键拉手
    uid = db.Column(db.Integer, db.ForeignKey('user.id'))
    # tips:设置外键,与文章表的主键拉手
    aid = db.Column(db.Integer, db.ForeignKey('article.id'))
    cdatetime = db.Column(db.DateTime, default=datetime.now)

    def __str__(self):
        return self.comment


#新增一张表,用于标注文章分类,一个分类下可以有多篇文章
class Article_type(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    typename = db.Column(db.String(30))
    articles = db.relationship('Article',backref='article_type')
