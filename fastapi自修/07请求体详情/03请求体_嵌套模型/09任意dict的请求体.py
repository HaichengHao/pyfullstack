# @Author    : 百年
# @FileName  :09任意dict的请求体.py
# @DateTime  :2025/8/21 16:44
'''
任意 `dict` 的请求体¶
你也可以将请求体声明为一个 `dict`，其中键为某种类型，值为另一种类型。

这样，你就不必事先知道有效的字段/属性名称是什么（就像使用 Pydantic 模型那样）。

如果你想接收事先不知道的键，这会很有用。

另一个有用的情况是，当你希望键是另一种类型（例如 `int`）时。

这就是我们接下来要看的。

在这种情况下，你将接受任何 `dict`，只要它具有 `int` 类型的键和 `float` 类型的值
'''

from fastapi import FastAPI

app = FastAPI()


@app.post("/index-weights/")
async def create_index_weights(weights: dict[int, float]):
    return weights

#important:
# 请记住，JSON 只支持 `str` 作为键。
# 但 Pydantic 具有自动数据转换功能。
# 这意味着，尽管你的 API 客户端只能发送字符串作为键，但只要这些字符串包含纯整数，Pydantic 就会对其进行转换和验证。
# 并且你作为 `weights` 接收到的 `dict` 实际上将具有 `int` 类型的键和 `float` 类型的值。


