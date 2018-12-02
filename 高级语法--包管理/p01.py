# 包含一个学生类，一个sayhello函数，一个打印语句

class Student():
    def __init__(self, name="NoName", age=18):
        self.name = name
        self.age = age

    def say(self):
        print("My name is {0}".format(self.name))

def sayhello():
    print("Hi,欢迎")

# 此判断语句建议一直作为程序的入口
# 当这个文件整个被导入使用时，就会执行print，例如：improt p01
# 如果只是被调用其中一部分，则不执行print，例如：from p01 import Student, sayhello
if __name__ == '__main__':
    print("这是模块p01")