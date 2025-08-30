# @Author    : 百年
# @FileName  :models.py
# @DateTime  :2025/8/28 17:32

from exts.extensions import db

class Goods(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    gname = db.Column(db.String(100),nullable=False)
    price = db.Column(db.Float,nullable=False)
    users = db.relationship('User',backref='goods_lst',secondary='user_goods')
    #important:多对多的话就需要写上secondary并跟上关系表,本案例中就是跟上了user_goods这张有了俩外键约束的表
    def __str__(self):
        return self.gname



#start_cb: 创建user与goods的关系表
class User_goods(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    goods_id = db.Column(db.Integer,db.ForeignKey('goods.id'))
    number = db.Column(db.Integer,default=1)
