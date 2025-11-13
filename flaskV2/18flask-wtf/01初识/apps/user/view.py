"""
@File    :view.py
@Editor  : 百年
@Date    :2025/10/29 10:44 
"""
from ..config import Config
from flask import Blueprint, request, render_template
from .form import UserForm
import os

user_bps = Blueprint(name='user', import_name=__name__)



@user_bps.route('/user', methods=['GET', 'POST'], endpoint='user')
def login():
    # 创建form对象uform
    uform = UserForm()
    if uform.validate_on_submit():  # 在提交的时候验证uform中的内容
        name = uform.name.data
        pwd = uform.pwd.data
        phone = uform.phone_num.data
        icon = uform.icon.data #tips:对于form数据的获得几乎总是通过form对象.属性(表单项).data来拿到数据
        print(icon)
        # < FileStorage: 'OIP-C.jpg'('image/jpeg') >
        print(icon.filename)  #就像之前的filestorge类型一样,又.filename方法可以让我们直接拿到图片名称


        icon_path = os.path.join(Config.UPLOAD_ICON_FOLDER, icon.filename)
        print(icon_path)
        uform.icon.data.save(icon_path)
    return render_template('user/login.html', uform=uform)
