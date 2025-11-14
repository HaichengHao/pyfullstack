"""
@File    :wsgi.py
@Editor  : 百年
@Date    :2025/11/14 11:55 
"""
from apps import create_app


if __name__ == '__main__':
    app = create_app()
    app.run()