# @Author    : 百年
# @FileName  :02声明带类型参数的list.py
# @DateTime  :2025/8/21 10:49
'''
要声明带有类型参数（内部类型）的类型，例如 `list`、`dict`、`tuple`

如果你的 Python 版本低于 3.9，请从 `typing` 模块导入其等效版本
使用方括号 `[` 和 `]` 将内部类型作为“类型参数”传递

'''
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results