# @Author    : 百年
# @FileName  :02自动转换.py
# @DateTime  :2025/8/22 13:40
'''
自动转换

Header 在 Path、Query 和 Cookie 提供的功能之上，还有一些额外的功能。

大多数标准请求头都由“连字符”字符分隔，也称为“减号”（-）。

但是像 user-agent 这样的变量在 Python 中是无效的。

因此，默认情况下，Header 会将参数名称中的下划线（_）字符转换为连字符（-），以提取和生成请求头文档。

此外，HTTP 请求头不区分大小写，因此你可以用标准的 Python 风格（也称为“snake_case”）声明它们。

所以，你可以在 Python 代码中像往常一样使用 user_agent，而不是需要将首字母大写为 User_Agent 或类似的形式。

如果出于某种原因你需要禁用下划线到连字符的自动转换，请将 Header 的参数 convert_underscores 设置为 False。
'''

from typing import Annotated

from fastapi import FastAPI, Header

app = FastAPI()


@app.get("/items/")
async def read_items(
    strange_header: Annotated[str | None, Header(convert_underscores=False)] = None,
):
    return {"strange_header": strange_header}

# 在将 convert_underscores 设置为 False 之前，请记住某些 HTTP 代理和服务器不允许使用包含下划线的请求头。