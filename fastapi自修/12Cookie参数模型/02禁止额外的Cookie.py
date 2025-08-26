# @Author    : 百年
# @FileName  :02禁止额外的Cookie.py
# @DateTime  :2025/8/22 14:19

'''
禁止额外的 Cookie¶
在某些特殊用例中（可能不常见），你可能希望限制你想要接收的 cookie。

你的 API 现在有了控制自身 cookie 同意 的能力。

您可以使用 Pydantic 的模型配置来 forbid 任何 extra 字段
'''

from fastapi import FastAPI, Cookie
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()


class Cookies(BaseModel):
    model_config = {'extra': 'forbid'}
    session_id: str
    fatebook_tracker: str | None = None
    googall_tracker: str | None = None


@app.get('/items/')
async def read_items(cookies: Annotated[Cookies, Cookie()]):
    return cookies


'''
如果客户端尝试发送一些额外 cookie，它们将收到一个错误响应。

可怜的 cookie 横幅，费尽心思想获得你的同意，结果却被 API 拒绝了。🍪

例如，如果客户端尝试发送一个值为 good-list-please 的 santa_tracker cookie，客户端将收到一个错误响应，告诉他们 santa_tracker cookie 是不允许的'''
