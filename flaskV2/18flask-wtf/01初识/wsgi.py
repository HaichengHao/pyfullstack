"""
@File    :wsgi.py
@Editor  : 百年
@Date    :2025/10/29 10:43 
"""

from apps import create_app


if __name__ == '__main__':
    app = create_app()
    app.run()