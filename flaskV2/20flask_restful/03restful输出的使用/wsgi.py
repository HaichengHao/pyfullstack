"""
@File    :wsgi.py
@Editor  : 百年
@Date    :2025/11/26 8:37 
"""
from flask import Flask
from apps import create_app

if __name__ == '__main__':
    app = create_app()
    app.run()