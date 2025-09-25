"""
@File    :02详谈UploadFile.py
@Editor  : 百年
@Date    :2025/9/24 20:43 
"""
import os.path

'''

UploadFile 具有以下属性

filename：一个 str 类型的原始上传文件名（例如 myimage.jpg）。
content_type：一个 str 类型的内容类型（MIME 类型 / 媒体类型）（例如 image/jpeg）。
file：一个 SpooledTemporaryFile（一个 文件类 对象）。这是实际的 Python 文件对象，你可以直接将其传递给其他期望 "文件类" 对象的函数或库。
UploadFile 具有以下 async 方法。它们都在底层调用相应的文件方法（使用内部的 SpooledTemporaryFile）。

write(data)：将 data（str 或 bytes）写入文件。
read(size)：读取文件中的 size（int）字节/字符。
seek(offset)：跳转到文件中的字节位置 offset（int）。
例如，await myfile.seek(0) 会跳转到文件的开头。
这在你执行一次 await myfile.read() 后需要再次读取内容时特别有用。
close()：关闭文件。
由于所有这些方法都是 async 方法，因此你需要 "await" 它们

'''
import os
from fastapi import FastAPI, UploadFile

app = FastAPI()


@app.post('/uploadfile')
async def uploadfile(file: UploadFile):
    # step1:判断目录是否存在
    upload_dir = './imgs'
    if not os.path.exists(upload_dir):
        os.mkdir(upload_dir)

    # step2:如果文件存在那么就构造传输文件保存的路径
    file_path = os.path.join(upload_dir, file.filename)

    # step3:读取上传的文件内容(bytes),并写入目标路径
    contents = await file.read()
    with open(file_path, 'wb') as f:
        f.write(contents)

    return {
        'filename': file.filename,
        'filesize': file.size,
        'content_type': file.content_type
    }
