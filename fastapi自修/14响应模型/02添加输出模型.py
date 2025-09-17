# @Author    : 百年
# @FileName  :02添加输出模型.py
# @DateTime  :2025/9/14 15:15
'''
我们可以改为创建一个包含明文密码的输入模型，以及一个不包含密码的输出模型
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
    # important:我们将 response_model 声明为我们的模型 UserOut，它不包含密码


@app.post('/user/', response_model=UserOut)
async def create_user(user: UserIn):  # important:在这里，即使我们的 *路径操作函数* 返回了包含密码的相同输入用户
    return user

'''
因此，**FastAPI** 将负责过滤掉输出模型中未声明的所有数据（使用 Pydantic）。

response_model 或返回类型¶
在这种情况下，由于两个模型不同，如果我们将函数返回类型注解为 UserOut，编辑器和工具会抱怨我们返回了无效类型，因为它们是不同的类。

这就是为什么在这个例子中我们必须在 response_model 参数中声明它。

...但请继续阅读下文，了解如何解决这个问题。
'''