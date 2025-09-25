"""
@File    :03快捷方式.py
@Editor  : 百年
@Date    :2025/9/22 23:15 
"""
'''
你不需要记住每个代码的含义。

你可以使用 `fastapi.status` 中的便捷变量。
'''
from fastapi import FastAPI, status

app = FastAPI()


@app.post('/items/', status_code=status.HTTP_201_CREATED)
async def create_item(name: str):
    return {'name': name}


'''
更改默认值¶
稍后，在高级用户指南中，你将看到如何返回与你在此处声明的默认状态码不同的状态码。'''
