"""
@File    :06带额外元数据的多文件上传.py
@Editor  : 百年
@Date    :2025/9/25 17:01 
"""
'''
与之前相同，你可以使用 File() 来设置额外参数，即使是针对 UploadFile 也可以
'''

from typing import Annotated
from fastapi import FastAPI,File,UploadFile
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.post('/files/')
async def create_files(
        files:Annotated[
            list[bytes],File(description="multiple files as bytes")
        ],
):
    return {
        'file_size':[
            len(file) for file in files
        ]
    }

@app.post('/uploadfiles/')
async def create_upload_files(
        files:Annotated[
            list[UploadFile],File(
                description="multiple files as UploadFiles"
            )
        ]
):
    return {
        'filenames':[
            file.filename for file in files
        ]
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
