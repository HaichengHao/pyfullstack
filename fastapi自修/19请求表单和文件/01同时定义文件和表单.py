"""
@File    :01同时定义文件和表单.py
@Editor  : 百年
@Date    :2025/9/25 17:26 
"""

# 你可以使用 File 和 Form 同时定义文件和表单字段。

from typing import Annotated
from fastapi import FastAPI,File,Form,UploadFile
app = FastAPI()

@app.post('/files/')
async def create_file(
        file:Annotated[bytes,File()],
        fileb:Annotated[UploadFile,File()],
        token:Annotated[str,Form()]

):
    return {
        'file_size':len(file),
        'token':token,
        'file_content_type':fileb.content_type
    }
'''
文件和表单字段将作为表单数据上传，你将收到文件和表单字段。

你可以将某些文件声明为 bytes 类型，将另一些文件声明为 UploadFile 类型。'''
'''
总结¶
当你需要在同一个请求中接收数据和文件时，请同时使用 File 和 Form。
'''