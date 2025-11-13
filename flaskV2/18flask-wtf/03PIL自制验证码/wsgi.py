"""
@File    :wsgi.py
@Editor  : 百年
@Date    :2025/11/9 11:23 
"""
from apps import create_app
from  flask_bootstrap import Bootstrap
if __name__ == '__main__':
    app =  create_app()
    app.run(debug=True)