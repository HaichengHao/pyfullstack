"""
@File    :dbhelper.py
@Editor  : 百年
@Date    :2025/11/17 13:14 
"""
from flask_sqlalchemy  import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
