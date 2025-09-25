"""
@File    :student.py
@Editor  : 百年
@Date    :2025/9/18 16:31 
"""
from fastapi import APIRouter, Form
from models import Student
from pydantic import BaseModel
from typing import Annotated

student_api = APIRouter()


class Student(BaseModel):
    name: str | None = None
    pwd: str | None = None
    sno: int | None = None
    clazz: str | None = None


# 查询所有学生
@student_api.get('/')
async def stuinfo():
    # important:注意使用了展开外键clazz__name
    all_stu_info = await Student.all().values('id', 'name', 'sno', 'clazz__name')  # [Student(),Student(),]
    return {
        'all_stu_info': all_stu_info
    }


# 添加学生
@student_api.post('/')
async def addstu(name: str = Form(), pwd: str = Form(), sno: str = Form(), clazz_id: str = Form()):
    # Student.create(
    #     name="张三"
    # )
    return {
        "name":name,
        "pwd":pwd,
        "sno":sno,
        "class_id":clazz_id
    }


# 查找单个学生
@student_api.get(
    '/{student_id}'
)
async def stuinfo_one(student_id: int):
    stuinfo_one = await Student.get(student_id)
    return {
        '学生信息': stuinfo_one
    }


# 编辑某个学生
@student_api.put(
    '/{student_id}'
)
async def mofy_stu(student_id: int):
    stu = await Student.get(student_id)
    if stu:
        newname = input('输入新的名称')
        stu.name = newname
    else:
        return '无此人'


# 删除某个学生
@student_api.delete(
    '/{student_id}'
)
async def del_stu(student_id: int):
    stu = await Student.get(student_id)
    if stu:
        await stu.delete()
