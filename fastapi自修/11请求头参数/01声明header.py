# @Author    : 百年
# @FileName  :01声明header.py
# @DateTime  :2025/8/22 10:52

from fastapi import FastAPI, Header

from typing import Annotated

app = FastAPI()


@app.get('/items/')
async def read_items(user_agent: Annotated[str | None, Header()] = None):
    return {
        'User-Agent': user_agent
    }
