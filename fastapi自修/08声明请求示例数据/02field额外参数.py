# @Author    : 百年
# @FileName  :02field额外参数.py
# @DateTime  :2025/8/21 18:59

#当pydantic模型中使用Field()时,可以声明额外的examples

from fastapi import FastAPI
from pydantic import BaseModel,Field
app = FastAPI()

class Item(BaseModel):
    name:str=Field(examples=['foo'])
    desc: str|None = Field(default=None,examples=['a very nice Item'])
    price:float=Field(examples=[35.4])
    tax:float|None = Field(default=None,examples=[3.2])

@app.put('/items/{item_id}')
async def update_item(
        item_id:int,
        item:Item
):
    results={'item_id':item_id,'item':item}
    return results

'''
JSON Schema - OpenAPI 中的 examples¶
当使用以下任何一个时：

Path()
Query()
Header()
Cookie()
Body()
Form()
File()
你还可以声明一组 examples，其中包含额外信息，这些信息将添加到 OpenAPI 内的 JSON Schemas 中。
'''