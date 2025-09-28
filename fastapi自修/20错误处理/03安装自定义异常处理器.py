"""
@File    :03安装自定义异常处理器.py
@Editor  : 百年
@Date    :2025/9/25 22:04 
"""
'''
您可以使用 Starlette 的相同异常工具添加自定义异常处理器。

假设您有一个自定义异常 UnicornException，您（或您使用的库）可能会 raise 它。

并且您希望使用 FastAPI 全局处理此异常。

您可以使用 @app.exception_handler() 添加自定义异常处理器'''

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


app = FastAPI()


#important:.exception_handler(这里头放自己定义的exception类)
@app.exception_handler(UnicornException)
async def unicorn_exception_handler(
        request: Request,
        exc: UnicornException
):
    return JSONResponse(
        status_code=418,
        content={
            'message': f'OOPS!!!{exc.name} did something, there goes a rainbow'
        }

    )


@app.get(
    '/unicorns/{name}'
)
async def read_unicorn(name: str):
    if name == 'yolo':
        raise UnicornException(name=name)
    return {
        'unicorn_name': name
    }
'''
在这里，如果您请求 /unicorns/yolo，*路径操作* 将 raise 一个 UnicornException。

但它将由 unicorn_exception_handler 处理。
'''