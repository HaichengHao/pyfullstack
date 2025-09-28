"""
@File    :01HTTPException.py
@Editor  : 百年
@Date    :2025/9/25 18:03 
"""
'''
在许多情况下，您需要向使用您 API 的客户端通知错误。

此客户端可以是带有前端的浏览器、其他人编写的代码、物联网设备等。

您可能需要告诉客户端，例如：

客户端没有足够的权限执行该操作。
客户端无法访问该资源。
客户端尝试访问的条目不存在。
等等。
在这些情况下，您通常会返回 **400** (从 400 到 499) 范围内的 **HTTP 状态码**。

这类似于 200 HTTP 状态码（从 200 到 299）。这些“200”状态码意味着请求某种程度上“成功”了。

400 范围内的状态码表示客户端发生错误。
'''

'''
要向客户端返回带有错误的 HTTP 响应，您可以使用 HTTPException。
'''
from fastapi import FastAPI, HTTPException

app = FastAPI()

items = {
    'foo': 'the foo wrestlers'
}


@app.get('/items/{item_id}')
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail='item not found')
    return {
        'item': items[item_id]
    }

'''
HTTPException 是一个普通的 Python 异常，它包含与 API 相关的额外数据。

因为它是一个 Python 异常，您不需要 return 它，而是 raise 它。

这也意味着，如果您在 *路径操作函数* 内部调用的某个实用函数中，并且在该实用函数内部抛出 HTTPException，它将不会运行 *路径操作函数* 的其余代码，而是会立即终止该请求并将 HTTPException 中的 HTTP 错误发送给客户端。

抛出异常而不是返回值的优势将在有关依赖和安全的部分中更加明显。

在此示例中，当客户端请求一个不存在的 ID 的项目时，抛出状态码为 404 的异常
'''