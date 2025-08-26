# @Author    : 百年
# @FileName  :01声明cookie参数.py
# @DateTime  :2025/8/22 10:46

'''
您可以像定义 Query 和 Path 参数一样定义 Cookie 参数。
'''
#导入
from fastapi import Cookie,FastAPI
from typing import Annotated

app = FastAPI()
@app.get('/items/')
async def read_items(ads_id:Annotated[str|None,Cookie()]=None): #声明cookie参数
    return {
        'ads_id':ads_id
    }
'''
Cookie 是 Path 和 Query 的“姐妹”类。它也继承自相同的通用 Param 类。
但请记住，当您从 fastapi 导入 Query, Path, Cookie 等时，它们实际上是返回特殊类的函数。
总结¶
使用 Cookie 声明 cookie，采用与 Query 和 Path 相同的通用模式'''