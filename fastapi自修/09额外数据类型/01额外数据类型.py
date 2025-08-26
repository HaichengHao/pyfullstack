# @Author    : 百年
# @FileName  :01额外数据类型.py
# @DateTime  :2025/8/22 9:53
'''
其他数据类型¶
以下是一些您可以使用的额外数据类型：

UUID:
一个标准的“通用唯一标识符”，在许多数据库和系统中常用作 ID。
在请求和响应中将表示为 str。
datetime.datetime:
一个 Python datetime.datetime 对象。
在请求和响应中将表示为 ISO 8601 格式的 str，例如：2008-09-15T15:53:00+05:00。
datetime.date:
Python datetime.date 对象。
在请求和响应中将表示为 ISO 8601 格式的 str，例如：2008-09-15。
datetime.time:
一个 Python datetime.time 对象。
在请求和响应中将表示为 ISO 8601 格式的 str，例如：14:23:55.003。
datetime.timedelta:
一个 Python datetime.timedelta 对象。
在请求和响应中将表示为总秒数的 float。
Pydantic 也支持将其表示为“ISO 8601 时间差编码”，更多信息请参阅文档。
frozenset:
在请求和响应中，与 set 的处理方式相同。
在请求中，将读取一个列表，消除重复项并将其转换为 set。
在响应中，set 将被转换为 list。
生成的 Schema 将指定 set 值是唯一的（使用 JSON Schema 的 uniqueItems）。
bytes:
标准的 Python bytes 对象。
在请求和响应中将视为 str。
生成的 Schema 将指定它是一个带有 binary “格式”的 str。
Decimal:
标准的 Python Decimal 对象。
在请求和响应中，与 float 的处理方式相同。
您可以在此处查看所有有效的 Pydantic 数据类型：Pydantic 数据类型。
'''

from datetime import datetime, time, timedelta
from typing import Annotated
from uuid import UUID
import uuid
from fastapi import Body, FastAPI,Query

app = FastAPI()
uid=uuid.uuid4()
print(uid)
@app.put("/items/{item_id}")
async def read_items(
    item_id: UUID,
    start_datetime: Annotated[datetime, Body()],
    end_datetime: Annotated[datetime, Body()],
    process_after: Annotated[timedelta, Body()],
    repeat_at: Annotated[time | None, Body()] = None,

):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "process_after": process_after,
        "repeat_at": repeat_at,
        "start_process": start_process,
        "duration": duration,
    }