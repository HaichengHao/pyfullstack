"""
@File    :01请求文件.py
@Editor  : 百年
@Date    :2025/9/24 9:21 
"""
from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()


@app.post('/files/')
# tips:创建文件参数的方式与创建 Body 或 Form 参数的方式相同
async def create_file(file: Annotated[bytes, File()]):
    return {'filesize': len(file)}


'''
File 是一个直接继承自 Form 的类。
但是请记住，当你从 fastapi 导入 Query, Path, File 等时，
它们实际上是返回特殊类的函数。
要声明文件主体，你需要使用 File，否则参数将被解释为查询参数或主体（JSON）参数
'''

'''
文件将作为 "表单数据" 上传。
如果你将路径操作函数参数的类型声明为 bytes，FastAPI 将为你读取文件，
你将收到 bytes 形式的内容。
请记住，这意味着整个内容将存储在内存中。这对于小文件来说效果很好。
但在某些情况下，你可能更倾向于使用 UploadFile'''


@app.post('/uploadfile/')
async def create_upload_file(file: UploadFile):
    return {'filename': file.filename,
            'filesize':file.size,
            'filetype':file.content_type
            }
