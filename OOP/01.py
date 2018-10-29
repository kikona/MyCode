
'''
定义一个学生类，用来形容学生
'''

# 定义一个空的类
class Student():
    # 一个空类，pass代表直接跳过
    # 此处pass必须要有
    pass

# 定义一个对象
mingyue = Student()

# 再定义一个类，用来描述听python的学生
class PythonStudent():
    # 用None给不确定的变量赋值
    name = None
    age = 18
    course = "Python"
    # 需要注意
    # def doHomework 的缩进层级
    # 系统默认有一个 self 参数
    def doHomework(self):
        print("我在做作业")

        # 推荐在函数末尾使用return语句
        return None

# 实例化一个叫 yueyue 的学生，是一个具体的人
yueyue = PythonStudent()
yueyue.name
yueyue.age

# 注意成员函数的调用，没有传递进入参数
yueyue.doHomework()