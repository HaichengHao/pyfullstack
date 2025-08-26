# @Author    : 百年
# @FileName  :01列表字段.py
# @DateTime  :2025/8/21 10:44
'''
请求体 - 嵌套模型¶
使用 FastAPI，你可以定义、验证、生成文档并使用任意深度嵌套的模型（感谢 Pydantic）
'''

#可以将属性定义为子类型,如 python 'list'

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name:str
    description:str|None = None
    price:float
    tax:float|None = None
    tags:list = [] #将tags指定为列表类型,默认是空列表
#     这将使 `tags` 成为一个列表，尽管它没有声明列表中元素的类型。

@app.put('/items/{item_id}')
async def update_item(item_id:int,item:Item):
    result = {
        'item_id':item_id,
        'item':item
    }
    return result

