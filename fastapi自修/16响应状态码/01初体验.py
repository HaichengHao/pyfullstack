"""
@File    :01初体验.py
@Editor  : 百年
@Date    :2025/9/22 22:58 
"""
'''
与指定响应模型的方式相同，你也可以在任何*路径操作*中使用参数 `status_code` 来声明用于响应的 HTTP 状态码

@app.get()
@app.post()
@app.put()
@app.delete()
等等。
'''

from fastapi import FastAPI
import uvicorn
app = FastAPI()

'''
请注意，`status_code` 是“装饰器”方法（`get`、`post` 等）的一个参数，而不是你的*路径操作函数*的参数，这与所有参数和请求体不同。'''

@app.post('/items', status_code=201)
async def create_item(name: str):
    return {'name': name}

if __name__ == '__main__':
    uvicorn.run('01初体验:app',reload=True,log_level='debug',host="127.0.0.1",port=8099)