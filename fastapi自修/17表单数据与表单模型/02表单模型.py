"""
@File    :02表单模型.py
@Editor  : 百年
@Date    :2025/9/24 9:04 
"""
from fastapi import FastAPI, Form

from pydantic import BaseModel
from typing import Annotated

app = FastAPI()


class FormData(BaseModel):
    username: str
    password: str
    model_config = {
        'extra':'forbid'
    }#tips:可以使用 Pydantic 的模型配置来 forbid 任何 extra 字段


@app.post('/login')
# tips: 您只需声明一个 Pydantic 模型，其中包含您希望作为 表单字段 接收的字段，然后将参数声明为 Form
async def login(data: Annotated[FormData, Form()]):
    return data
