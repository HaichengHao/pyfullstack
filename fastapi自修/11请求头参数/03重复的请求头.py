# @Author    : 百年
# @FileName  :03重复的请求头.py
# @DateTime  :2025/8/22 13:43
'''
可能会收到重复的请求头。这意味着同一个请求头有多个值。

你可以在类型声明中使用列表来定义这些情况。

你将以 Python list 的形式接收所有重复请求头的值。

例如，要声明一个可以多次出现的 X-Token 请求头，你可以这样写:
'''
from typing import Annotated

from fastapi import FastAPI, Header

app = FastAPI()


#其实就是接收列表数据
@app.get("/items/")
async def read_items(x_token: Annotated[list[str] | None, Header()] = None):
    return {"X-Token values": x_token}

'''
总结¶
使用 Header 声明请求头，采用与 Query、Path 和 Cookie 相同的通用模式。

并且不用担心变量中的下划线，FastAPI 会负责转换它们。'''