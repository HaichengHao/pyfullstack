# @Author    : 百年
# @FileName  :01Field的使用.py
# @DateTime  :2025/8/20 18:07

'''
就像你可以使用 Query、Path 和 Body 在路径操作函数参数中声明额外的验证和元数据一样，
你也可以使用 Pydantic 的 Field 在 Pydantic 模型!!!内部声明验证和元数据。
'''
# important:注意,field是在pydantic模型中用的，Q\P\B是在路径参数中用的

from typing import Annotated
from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str
    #start_cb: 声明模型属性,将field与模型属性一起使用
    description: str | None = Field(
        default=None,
        title='the description of the item',
        max_length=300
    )
    price: float = Field(
        gt=0,
        description='价格必须大于0'
    )
    #end_cb:声明模型属性结束
    tax: str | None = None

@app.put('/items/{item_id}')
async def update_item(item_id:int,item:Annotated[Item,Body(embed=True)]):
    results = {
        'item_id':item_id,
        'item':item
    }
    return results
'''
请注意，Field 是直接从 pydantic 导入的，而不是像其他所有（Query、Path、Body 等）一样从 fastapi 导入。
Field 的工作方式与 Query、Path 和 Body 相同，它具有所有相同的参数等。
实际上，你接下来会看到的 Query、Path 和其他对象都是一个通用 Param 类的子类，而 Param 类本身又是 Pydantic 的 FieldInfo 类的子类。

Pydantic 的 Field 也返回一个 FieldInfo 的实例。

Body 也直接返回 FieldInfo 子类的对象。你稍后还会看到其他一些 Body 类的子类。

请记住，当你从 fastapi 导入 Query、Path 和其他对象时，它们实际上是返回特殊类的函数。

请注意，每个带有类型、默认值和 Field 的模型属性，其结构都与*路径操作函数*的参数相同，只是用 Field 代替了 Path、Query 和 Body。
'''