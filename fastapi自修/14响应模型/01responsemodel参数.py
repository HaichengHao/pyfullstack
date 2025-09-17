# @Author    : 百年
# @FileName  :01responsemodel参数.py
# @DateTime  :2025/9/14 10:46
from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float
    tags: list[str] = []


@app.post('/items/', response_model=Item)
async def create_item(item: Item) -> Any:
    return item


@app.get('/items/', response_model=list[Item])
async def read_items() -> Any:
    return [
        {'name': 'foo', 'price': 20.0},
        {'name': 'bar', 'price': 12.0},
    ]


'''
response_model 优先级¶
如果你同时声明了返回类型和 response_model，response_model 将优先被 FastAPI 使用。

这样，即使你返回的类型与响应模型不同，你也可以为你的函数添加正确的类型注解，供编辑器和 mypy 等工具使用。同时，你仍然可以让 FastAPI 使用 response_model 进行数据验证、文档生成等工作。

你也可以使用 response_model=None 来禁用该 *路径操作* 的响应模型创建，如果你正在为非有效 Pydantic 字段的事物添加类型注解，你可能需要这样做，你将在下面的一个章节中看到一个示例。

'''
