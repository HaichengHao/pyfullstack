"""
@File    :19详细剖析上下文.py
@Editor  : 百年
@Date    :2025/12/11 16:44 
"""

class Foo(object):
    def __enter__(self):
        return 'hehe'
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass



#tips:
# with 后面跟的是对象,as后面就是这个对象的返回值
func=Foo()
with func as f:
    print(f)
'''
D:\venvs\converse_pyspider\Scripts\python.exe E:\pyfullstack\02python高阶\19详细剖析上下文.py 
hehe

Process finished with exit code 0

其实我们用with  open() as f 
管理上下文的时候本质也是这样的,先用open打开一个files对象,然后f就是files对象的返回值 ，然后我们可以用f来进行f.write,f.close这样的功能
'''