# @Author    : 百年
# @FileName  :03集合类型.py
# @DateTime  :2025/8/21 11:19
'''
集合类型
但我们仔细考虑后发现，标签不应该重复，它们可能应该是唯一的字符串。

Python 也有一个特殊的数据类型用于表示唯一项的集合，即 `set`。

然后我们可以将 `tags` 声明为字符串集合
'''

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name:str
    description:str|None=None
    price:float
    tax:float|None=None
    tags:set[str]=set()

@app.put('/items/{item_id}')
async def update_item(item_id:int,item:Item):
    result={
        'item_id':item_id,
        'item':Item
    }
    return result
'''
这样，即使你收到带有重复数据的请求，它也会被转换为一个包含唯一项的集合。

并且无论何时你输出该数据，即使源数据有重复，它也会作为唯一项的集合输出。

它也会被相应地注解/文档化。'''