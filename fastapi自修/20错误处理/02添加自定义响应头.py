"""
@File    :02添加自定义响应头.py
@Editor  : 百年
@Date    :2025/9/25 21:54 
"""
'''
在某些情况下，向 HTTP 错误添加自定义响应头非常有用。例如，用于某些类型的安全。

您可能不需要在代码中直接使用它。

但如果您需要它用于高级场景，可以添加自定义响应头。
'''

from fastapi import FastAPI, HTTPException

app = FastAPI()

items = {
    'foo': 'the foo wrestlers'
}


@app.get('/items-header/{item_id}')
async def read_item_header(item_id: str):
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail='item not found',
            headers={
                'X-Error': 'There goes my error'
            }
        )
    return {
        'item': items[item_id]
    }

