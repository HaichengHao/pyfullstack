# @Author    : 百年
# @FileName  :08纯列表请求体.py
# @DateTime  :2025/8/21 16:42
'''
如果你期望的 JSON 请求体的顶层值是 JSON `array` (Python `list`)，
你可以在函数参数中声明其类型，与在 Pydantic 模型中一样

'''
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


@app.post("/images/multiple/")
async def create_multiple_images(images: list[Image]):
    return images