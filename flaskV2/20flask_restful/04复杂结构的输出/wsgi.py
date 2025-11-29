"""
@File    :wsgi.py
@Editor  : 百年
@Date    :2025/11/28 10:00 
"""


from apps import create_app


if __name__ == '__main__':
    app = create_app()
    app.run()