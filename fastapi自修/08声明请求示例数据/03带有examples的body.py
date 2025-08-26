# @Author    : 百年
# @FileName  :03带有examples的body.py
# @DateTime  :2025/8/22 9:18

from typing import Annotated
from fastapi import FastAPI,Body
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name:str
    description:str|None=None
    price:float
    tax:float|None=None

@app.put('/items/{item_id}')
async def update_item(
        item_id:int,
        item:Annotated[
            Item,
            Body(
                examples=[
                    {
                        "name": "Foo",
                        "description": "A very nice Item",
                        "price": 35.4,
                        "tax": 3.2,
                    }
                ]
            )
        ]
):
    results = {"item_id": item_id, "item": item}
    return results