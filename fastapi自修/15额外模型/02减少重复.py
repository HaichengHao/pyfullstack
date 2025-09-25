"""
@File    :02减少重复.py
@Editor  : 百年
@Date    :2025/9/21 14:32 
"""
'''
减少重复¶
减少代码重复是 FastAPI 的核心理念之一。

因为代码重复会增加出现 bug、安全问题、代码不同步问题（当你在一个地方更新但在其他地方没有更新时）等的几率。

而且这些模型都共享大量数据，并且重复了属性名称和类型。

我们可以做得更好。

我们可以声明一个 UserBase 模型作为其他模型的基础。然后我们可以创建该模型的子类，这些子类会继承其属性（类型声明、验证等）。

所有数据转换、验证、文档等都将正常工作。

这样，我们就可以只声明模型之间的差异（带明文 password、带 hashed_password 和不带密码）。
'''
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    pass


class UserInDB(UserBase):
    hashed_password: str


def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password


def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    print("User saved! ..not really")
    return user_in_db


@app.post("/user/", response_model=UserOut)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved
