# @Author    : 百年
# @FileName  :01声明请求示例数据.py
# @DateTime  :2025/8/21 17:35

'''
你可以声明你的应用可以接收的数据示例。

以下是几种实现方法。

Pydantic 模型中的额外 JSON Schema 数据
你可以为一个 Pydantic 模型声明 examples，这些示例将被添加到生成的 JSON Schema 中。

'''

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

    model_config = {
        'json_schema_extra':{
            'examples':[
                {
                    'name':'foo',
                    'desc':'a very nice item',
                    'price':35.4,
                    'tax':3.2
                }
            ]
        }
    }

@app.put('/items/{item_id}')
async def update_item(item_id:int,item:Item):
    results={
        'item_id':item_id,
        'item':item
    }
    return results

'''
这样设置之后editvalue中就是
[
                {
                    'name':'foo',
                    'desc':'a very nice item',
                    'price':35.4,
                    'tax':3.2
                }
            ]
            该额外信息将原样添加到该模型的输出 JSON Schema 中，并将在 API 文档中使用
'''
