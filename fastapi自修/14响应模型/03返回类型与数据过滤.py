# @Author    : 百年
# @FileName  :03返回类型与数据过滤.py
# @DateTime  :2025/9/14 15:25


'''
让我们继续前面的例子。我们想用**一种类型来注解函数**，但我们希望能够从函数返回实际包含**更多数据**的内容。

我们希望 FastAPI 使用响应模型继续**过滤**数据。这样，即使函数返回了更多数据，响应也只会包含响应模型中声明的字段。

在前面的例子中，因为类是不同的，我们不得不使用 response_model 参数。但这同时也意味着我们无法获得编辑器和工具对函数返回类型检查的支持。

但在大多数需要这样做的情况下，我们希望模型只是像本例一样**过滤/移除**部分数据。

在这些情况下，我们可以使用类和继承来利用函数的**类型注解**，从而在编辑器和工具中获得更好的支持，并且仍然获得 FastAPI 的**数据过滤**能力。
'''


from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class BaseUser(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class UserIn(BaseUser):
    password: str


@app.post("/user/")
async def create_user(user: UserIn) -> BaseUser:
    return user

'''
通过这种方式，我们获得了编辑器和 mypy 等工具的支持，因为此代码在类型方面是正确的，同时我们也获得了 FastAPI 的数据过滤功能。

这是如何工作的？让我们来了解一下。🤓

类型注解与工具支持¶
首先让我们看看编辑器、mypy 和其他工具会如何看待这一点。

BaseUser 包含基础字段。然后 UserIn 继承自 BaseUser 并添加了 password 字段，因此它将包含两个模型的所有字段。

我们将函数返回类型注解为 BaseUser，但我们实际上返回的是一个 UserIn 实例。

编辑器、mypy 和其他工具不会对此抱怨，因为在类型方面，UserIn 是 BaseUser 的子类，这意味着当预期是任何 BaseUser 类型时，它是一个 *有效* 类型。'''