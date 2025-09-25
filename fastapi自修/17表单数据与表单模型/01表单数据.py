"""
@File    :01初体验.py
@Editor  : 百年
@Date    :2025/9/23 23:03 
"""
'''
当您需要接收表单字段而不是 JSON 时，您可以使用 Form。
'''
from typing import Annotated
from fastapi import FastAPI,Form
import uvicorn

app = FastAPI()

@app.post('/login/')
async def login(username:Annotated[str,Form(description="用户名")],password:Annotated[str,Form()]):
    return {
        'username':username
    }
if __name__ == '__main__':

    uvicorn.run('01初体验:app',reload=True,log_level='debug',host='127.0.0.1',port=8099)

'''
使用 Form，您可以声明与 Body（以及 Query、Path、Cookie）相同的配置，
包括验证、示例、别名（例如 user-name 而不是 username）等。
Form 是一个直接继承自 Body 的类。
'''

