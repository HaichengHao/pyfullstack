# @Author    : 百年
# @FileName  :04FastAPI数据过滤.py
# @DateTime  :2025/9/14 15:41
'''
FastAPI 数据过滤¶
现在，对于 FastAPI，它将查看返回类型并确保你返回的内容**只**包含该类型中声明的字段。

FastAPI 在内部与 Pydantic 协同完成多项工作，以确保类继承的那些规则不被用于返回数据过滤，否则你最终可能会返回比预期多得多的数据。

通过这种方式，你可以两全其美：既有带**工具支持**的类型注解，又有**数据过滤**。
'''


from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None


class UserOut(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


@app.post("/user/", response_model=UserOut)
async def create_user(user: UserIn) -> Any:
    return user