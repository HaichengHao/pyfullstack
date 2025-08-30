# @Author    : 百年
# @FileName  :view.py
# @DateTime  :2025/8/27 16:50

from flask import Blueprint, request, render_template
from apps.user.models import User
from apps.article.models import Article
from exts.extensions import db

article_bp = Blueprint(name='article', import_name=__name__)


@article_bp.route('/publish', methods=['POST', 'GET'], endpoint='publish')
def article_publish():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        uid = request.form.get('uid')
        article = Article()
        article.title = title
        article.content = content
        article.user_id = uid
        db.session.add(article)
        db.session.commit()
        return '添加成功'

    users = User.query.filter(User.isdelete == False).all()
    return render_template('article/add_article.html',users=users)

@article_bp.route('/all_article',methods=['POST','GET'],endpoint='all_article')
def article_all():
    if request.method == 'POST':
        pass

    all_article = Article.query.all()
    return render_template('article/all.html',all_article=all_article)


@article_bp.route('/all1',endpoint='all1')
def all_article():
    id = request.args.get('id')
    user = User.query.get(id)
    return render_template('article/all1.html',user=user)
