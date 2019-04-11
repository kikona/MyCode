
screen_size = 40        # 屏幕大小
# 创建分数
second = 0

class Functions:

    @staticmethod
    def is_in_list(list, x, y):
        for i in list:
            if x == i.x and y == i.y:
                return True
        return False

    @staticmethod
    def fenshu():
        global second
        second += 1