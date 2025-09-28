"""
@File    :04覆盖默认异常处理器.py
@Editor  : 百年
@Date    :2025/9/28 16:31 
"""
'''
**FastAPI** 有一些默认的异常处理器。

这些处理器负责在您 raise HTTPException 和请求包含无效数据时返回默认的 JSON 响应。

您可以用自己的异常处理器覆盖这些默认处理器。

覆盖请求验证异常¶
当请求包含无效数据时，**FastAPI** 内部会抛出 RequestValidationError。

并且它还包含一个默认的异常处理器。

要覆盖它，请导入 RequestValidationError 并使用 @app.exception_handler(RequestValidationError) 来装饰异常处理器。

异常处理器将接收一个 Request 和该异常。
'''

from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()



'''
覆盖 HTTPException 错误处理器¶
同样，您可以覆盖 HTTPException 处理器。

例如，您可能希望为这些错误返回纯文本响应而不是 JSON
'''

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)

'''
RequestValidationError 是 Pydantic 的 ValidationError 的子类。

**FastAPI** 使用它，以便如果您在 response_model 中使用了 Pydantic 模型，并且您的数据有错误，您将在日志中看到该错误。

但客户端/用户不会看到它。相反，客户端将收到一个 HTTP 状态码为 500 的“内部服务器错误”。

应该如此，因为如果您的 *响应* 或代码中的任何位置（而不是在客户端的 *请求* 中）存在 Pydantic ValidationError，那实际上是您代码中的一个错误。

在您修复它时，您的客户端/用户不应该访问有关错误的内部信息，因为这可能会暴露安全漏洞
'''
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id == 3:
        raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
    return {"item_id": item_id}