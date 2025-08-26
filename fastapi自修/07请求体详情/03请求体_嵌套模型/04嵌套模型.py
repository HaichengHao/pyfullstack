# @Author    : 百年
# @FileName  :04嵌套模型.py
# @DateTime  :2025/8/21 11:23

'''
嵌套模型
Pydantic 模型的每个属性都有一个类型。

但该类型本身可以是另一个 Pydantic 模型。

因此，你可以声明具有特定属性名称、类型和验证的深度嵌套 JSON “对象”。

所有这些都可以任意嵌套。

定义子模型¶
例如，我们可以定义一个 `Image` 模型
'''
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Image(BaseModel):
    url:str
    name:str

class Item(BaseModel):
    name:str
    desc:str|None=None
    price:float
    tax:float
    image:Image|None=None #将子模型用作类型


@app.put('/items/{item_id}')
async def update_item(item_id:int,item:Item):
    results={
        'item_id':item_id,
        'item':item
    }
    return results

'''
这意味着 FastAPI 将期望一个类似于以下的请求体
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2,
    "tags": ["rock", "metal", "bar"],
    "image": {
        "url": "http://example.com/baz.jpg",
        "name": "The Foo live"
    }
}
'''