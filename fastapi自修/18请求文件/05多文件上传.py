"""
@File    :05多文件上传.py
@Editor  : 百年
@Date    :2025/9/24 21:54 
"""
'''
多文件上传¶
可以同时上传多个文件。
它们将关联到使用 "表单数据" 发送的同一个 "表单字段"。
要使用此功能，请声明一个 bytes 或 UploadFile 的列表
'''

from typing import Annotated
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.post('/files/')
async def create_files(files: Annotated[list[bytes], File()]):
    return {
        'file_sizes': [len(file) for file in files]
    }


@app.post('/uploadfiles/')
async def create_upload_files(files: list[UploadFile]):
    return {
        'filenames': [file.filename for file in files]

    }


@app.get('/')
async def main():
    content = """
    <body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)
