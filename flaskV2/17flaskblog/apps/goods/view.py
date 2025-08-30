# @Author    : 百年
# @FileName  :view.py
# @DateTime  :2025/8/28 21:22

from flask import Blueprint, request, render_template
from exts.extensions import db
from apps.goods.models import Goods, User_goods
from apps.user.models import User

goods_bp = Blueprint(name='goods', import_name=__name__)


# 用户找商品
@goods_bp.route('/findgoods', endpoint='findgoods')
def findgoods_route():
    uid = request.args.get('uid')
    user = User.query.get(uid)
    return render_template('goods/findgoods.html',user=user)



# 根据商品找用户
@goods_bp.route('/finduser', endpoint='finduser')
def findusers_route():
    gid = request.args.get('gid')
    goods = Goods.query.get(gid) #查询到商品名称
    return render_template('goods/finduser.html',goods=goods)


# 用户买商品

@goods_bp.route('/show', endpoint='purchase')
def show_route():
    users = User.query.filter(User.isdelete==False).all()
    goods = Goods.query.all()
    return render_template('goods/show.html', users=users, goods=goods)


@goods_bp.route('/buy', endpoint='buy')
def buy_route():
    uid = request.args.get('uid')
    gid = request.args.get('gid')
    Ug = User_goods()  # 创建表对象
    Ug.user_id = uid
    Ug.goods_id = gid
    db.session.add(Ug)
    db.session.commit()
    return "购买成功"
