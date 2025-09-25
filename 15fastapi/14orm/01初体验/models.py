"""
@File    :01初体验.py
@Editor  : 百年
@Date    :2025/9/18 12:13 
"""

#important:pip install tortoise-orm 注意别装错了！！！！
# 进行数据库迁移的时候用的是
from tortoise.models import Model
from tortoise import fields


class Student(Model):
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=32, description='姓名')
    pwd = fields.CharField(max_length=32, description="密码")
    sno = fields.IntField(description="学号")

    # important:描述一对多的关系
    clazz = fields.ForeignKeyField("models.Clazz", related_name="students")

    #important:描述多对多的关系,一个学生可以选多门课，一门课可以对应多个学生
    courses = fields.ManyToManyField("models.Course",related_name="students")


class Clazz(Model):
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=32, description="班级名称")


class Course(Model):
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=32, description="课程名称")
    teacher = fields.ForeignKeyField("models.Teacher",related_name="courses")
    caddr = fields.CharField(max_length=32,description="教室",default=None)

class Teacher(Model):
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=32,description="教师姓名")
    pwd = fields.CharField(max_length=32,description="密码")
    tno = fields.IntField(description="教师号")

