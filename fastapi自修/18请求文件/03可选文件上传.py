"""
@File    :03可选文件上床.py
@Editor  : 百年
@Date    :2025/9/24 21:14 
"""
# 你可以通过使用标准类型注解并将默认值设置为 None 来使文件可选

from typing import Annotated

from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/files/")
async def create_file(file: Annotated[bytes | None, File()] = None):
    if not file:
        return {"message": "No file sent"}
    else:
        return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile | None = None):
    if not file:
        return {"message": "No upload file sent"}
    else:
        return {"filename": file.filename}