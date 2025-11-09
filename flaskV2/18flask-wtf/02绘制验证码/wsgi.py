"""
@File    :wsgi.py
@Editor  : 百年
@Date    :2025/11/2 21:28 
"""
from apps import create_app

if __name__ == '__main__':
    app = create_app()
    app.run()