"""
@File    :01多个模型.py
@Editor  : 百年
@Date    :2025/9/21 11:53 
"""
'''
接着上一个例子，通常会有一个实体有多个相关的模型。

对于用户模型尤其如此，因为

输入模型需要包含密码。
输出模型不应包含密码。
数据库模型可能需要包含哈希密码。

绝不要存储用户的明文密码。始终存储一个可以验证的“安全哈希值”。

如果你不了解，你将在安全章节中学习“密码哈希”是什么。
'''

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


class UserInDB(BaseModel):
    username: str
    hashed_password: str
    email: EmailStr
    full_name: str | None = None


def fake_password_hasher(raw_password: str):
    return "superssecret" + raw_password


def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    '''
    因为 user_in.dict() 是一个 dict（字典），然后我们通过在它前面加上 ** 并将其传递给 UserInDB 来让 Python“解包”它。

    因此，我们从另一个 Pydantic 模型中的数据创建了一个 Pydantic 模型。
    
    解包 dict 和额外关键字参数¶
    然后添加额外的关键字参数 hashed_password=hashed_password，就像这样：'''
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    print('User saved!..not really')
    return user_in_db


'''
在 Pydantic v1 中，该方法名为 .dict()，在 Pydantic v2 中被弃用（但仍受支持），并更名为 .model_dump()。

这里的示例使用 .dict() 以兼容 Pydantic v1，但如果可以使用 Pydantic v2，则应改用 .model_dump()。
'''


@app.post('/user/', response_model=UserOut)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved
