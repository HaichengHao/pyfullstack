# @Author    : 百年
# @FileName  :05特殊类型和验证.py
# @DateTime  :2025/8/21 16:34
'''
除了 `str`、`int`、`float` 等普通单一类型外，你还可以使用从 `str` 继承的更复杂的单一类型。

要查看所有可用选项，请查阅 Pydantic 的类型概述。你将在下一章看到一些示例。

例如，在 `Image` 模型中我们有一个 `url` 字段，我们可以将其声明为 Pydantic 的 `HttpUrl` 实例而不是 `str`
'''
from fastapi import FastAPI
from pydantic import BaseModel,HttpUrl

app = FastAPI()

class Image(BaseModel):
    url:HttpUrl #该字符串将被检查是否为有效的 URL，并相应地在 JSON Schema / OpenAPI 中进行文档化。
    name:str

class Item(BaseModel):
    name:str
    price:float
    tax:float
    tags:set[str] = set()
    image:Image|None=None

@app.put('/items/{item_id}')
async def update_item(item_id:int,item:Item):
    results={
        'item_id':item_id,
        'item':item
    }
    return results

