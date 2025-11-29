"""
@File    :dbhelper.py
@Editor  : 百年
@Date    :2025/11/28 10:01 
"""
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
