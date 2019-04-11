# 飞机类
import DisplayMode
import Option

class airplay(DisplayMode.Displayed):
    def __init__(self):
        # 飞机拥有自己的坐标
        self.__points = [
            DisplayMode.Point(39, 18),
            DisplayMode.Point(39, 19),
            DisplayMode.Point(38, 19),
            DisplayMode.Point(39, 20)
        ]

    # 重写父类方法，返回自己的坐标
    def get_point_list(self):
        return self.__points

    # 左移
    def move_left(self):
        for i in self.__points:
            if i.y > 0:
                i.y -= 1
            else:
                return

    # 右移
    def move_right(self):
        for i in self.__points[::-1]:
            if i.y < Option.screen_size - 1:
                i.y += 1
            else:
                return

# 单个子弹的类
class Bullet(DisplayMode.Displayed):
    def __init__(self):
        self.__point = []       # 坐标
        self.active = False

    # 设置子弹的坐标
    def set_point(self, start_point):
        self.__point = [
            start_point,
            DisplayMode.Point(start_point.x + 1, start_point.y),
            DisplayMode.Point(start_point.x + 2, start_point.y)
        ]

    # 子弹可以飞
    def bullet_fall(self):
        for i in self.__point:
            i.x -= 3
            if i.x < -5:
                self.active = False

    # 返回自己的坐标
    def get_point_list(self):
        return self.__point



# 管理子弹的类
class BulletManager(DisplayMode.Displayed):
    def __init__(self, jet):
        self.__bullet_list = []
        self.__jet = jet

        # 创建8发子弹
        for i in range(8):
            bullet = Bullet()
            bullet.active = False  # 位置由飞机头确定，不在这里设置
            self.__bullet_list.append(bullet)

    # 从失效的子弹中，选一个激活
    def create_bullet(self):
        for i in self.__bullet_list:
            if not i.active:
                i.active = True
                # 将飞机头的位置设置为子弹的初始位置
                point = self.__jet.get_point_list()[-2]
                i.set_point(DisplayMode.Point(point.x - 5, point.y))
                return

    # 所有激活状态的子弹飞
    def all_bullet_fall(self):
        for i in self.__bullet_list:
            if i.active:
                i.bullet_fall()

    # 返回所有子弹的坐标
    def get_point_list(self):
        all_bullet_point = []
        for i in self.__bullet_list:
            all_bullet_point += i.get_point_list()
        return all_bullet_point

    # 管理所有子弹飞
    def action(self):
        self.all_bullet_fall()

    # 返回所有子弹，为了检测是否击中
    def get_bullet_list(self):
        return self.__bullet_list
