# @Author    : 百年
# @FileName  :01定义请求头参数.py
# @DateTime  :2025/8/22 14:32

from fastapi import FastAPI, Header

from pydantic import BaseModel

from typing import Annotated

app = FastAPI()


class CommonHeaders(BaseModel):
    model_config = {'extra': 'forbid'}  # 禁止额外请求头
    host: str
    save_data: bool
    if_modified_since: str | None = None
    traceparent: str | None = None
    x_tag: list[str] = []


@app.get('/items/')
async def read_items(headers: Annotated[CommonHeaders, Header(convert_underscores=False)]):  # 禁用下划线转换
    return headers
