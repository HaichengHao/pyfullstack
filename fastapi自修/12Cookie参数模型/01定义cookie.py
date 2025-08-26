# @Author    : 百年
# @FileName  :01定义cookie.py
# @DateTime  :2025/8/22 13:47
'''
如果你有一组相关的 cookie，你可以创建一个 Pydantic 模型 来声明它们。🍪

这将允许您在多个地方重用模型，并且可以一次性为所有参数声明验证和元数据。
'''

from typing import Annotated
from fastapi import FastAPI,Cookie
from pydantic import BaseModel

app = FastAPI()

class Cookies(BaseModel):
    session_id:str
    fateback_tracker:str|None=None
    googall_tracker:str|None=None

@app.get('/items/')
async def read_items(
        cookies:Annotated[Cookies,Cookie()]
):
    return cookies

'''
FastAPI 将从请求中接收到的 cookie 中 提取每个字段 的数据，并为你提供你定义的 Pydantic 模型。
'''