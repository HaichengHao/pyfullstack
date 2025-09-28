"""
@File    :05使用RequestValidationError的响应体.py
@Editor  : 百年
@Date    :2025/9/28 21:13 
"""
'''
RequestValidationError 包含它收到的包含无效数据的 body。

您可以在开发应用程序时使用它来记录响应体并进行调试，将其返回给用户等'''

from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder(
            {"detail": exc.errors(),
             "body": exc.body}
        )
    )


class Item(BaseModel):
    title: str
    size: int


@app.post("/items")
async def create_item(item: Item):
    return item
