import Option
import os
# 点类
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

# 为了统一接口返回自己坐标，而设置的类
class Displayed:
    def get_point_list(self):
        pass

# 显示器类，可以显示任何图案
class Displayer:
    def __init__(self):
        self.__list = []  # 通过列表管理所有图案

    # 添加显示图案
    def add_item(self, item: Displayed):
        self.__list.append(item)

    # 显示所有的点
    def reflash(self):
        # 首先收集所有图案的点
        list_point = []
        for i in self.__list:
            # 所有图案通过get_point_list()方法返回自己的坐标
            list_point += i.get_point_list()

        # 确定点在屏幕的位置
        point_str = ""
        for i in range(Option.screen_size):
            for j in range(Option.screen_size):
                # 通过静态方法判断所有点在的位置
                if Option.Functions.is_in_list(list_point, i, j):
                    point_str += "回"
                else:
                    point_str += "  "
            # 换行
            point_str += "\n"

        # 先清屏后显示
        os.system("cls")
        print(point_str[:-1])
        print("==" * Option.screen_size)
        print("当前分数为：",Option.second)
