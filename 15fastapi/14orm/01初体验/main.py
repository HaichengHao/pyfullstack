"""
@File    :main.py
@Editor  : 百年
@Date    :2025/9/18 12:53 
"""
from fastapi import FastAPI
import uvicorn
from tortoise.contrib.fastapi import register_tortoise  # important:用这个来进行数据库迁移
from models import *
from settings import TORTOISE_ORM
from api.student import student_api

app = FastAPI()

# 注册路由
app.include_router(student_api,prefix='/student')
# 该方法会在fastapi启动时触发,内部通过传递进去的app对象,监听服务启动和终止事件
register_tortoise(
    app=app,
    config=TORTOISE_ORM,
    generate_schemas=True,  # 如果数据库为空,则自动生成对应表单,生产环境不要开
    # add_exception_handlers=True,#生产环境不要开,会泄露调试信息
    # config={
    #     'connections': {
    #         'default': {
    #             'engine': 'tortoise.backends.mysql',
    #             'credentials': {
    #                 'host': '127.0.0.1',
    #                 'port': '3306',
    #                 'user': 'root',
    #                 'password': 'HHCzio20',
    #                 'database': 'fastapi',
    #                 'minsize': 1,
    #                 'maxsize': 5,
    #                 'charset': 'utf8mb4',
    #                 'echo': True
    #
    #             }
    #         }
    #     },
    #     'apps': {
    #         'models': {
    #             'models': ['models'],
    #             'default_connection': 'default',
    #         }
    #     },
    #     'use_tz':False,
    #     'timezone':'Asia/Shanghai'
    # }
)

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8099, reload=True, log_level='debug')
