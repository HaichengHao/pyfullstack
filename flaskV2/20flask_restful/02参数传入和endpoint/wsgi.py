"""
@File    :wsgi.py
@Editor  : 百年
@Date    :2025/11/17 13:14 
"""

from apps import create_app

if __name__ == '__main__':
    app = create_app()
    app.run()