# @Author    : 百年
# @FileName  :05响应模型编码参数.py
# @DateTime  :2025/9/14 15:53
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.5
    tags: list[str] = []
'''
description: Union[str, None] = None（或 Python 3.10 中的 str | None = None）的默认值为 None。
tax: float = 10.5 的默认值为 10.5。
tags: List[str] = [] 的默认值为空列表：[]。
但如果它们实际上并未存储，你可能希望在结果中省略它们。

例如，如果你的 NoSQL 数据库中有许多带可选属性的模型，但你不想发送包含大量默认值的超长 JSON 响应
'''

items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}

#important:使用 response_model_exclude_unset 参数
@app.get("/items/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]
'''
这些默认值将不会包含在响应中，只会包含实际设置的值。

因此，如果你向 ID 为 foo 的项的 *路径操作* 发送请求，响应（不包含默认值）将是
{
    "name": "Foo",
    "price": 50.2
}
'''

#tips: response_model_exclude_unset=True 意为排除未设置的值,True为排除,False为不排除,设置为True就是显示所有 有的 没有的一律不显示
# response_model_exclude_defaults 去除掉有默认值的,但是如果写入了值,那就返回
# response_model_exclude_none 排除为None的值,但是有就返回