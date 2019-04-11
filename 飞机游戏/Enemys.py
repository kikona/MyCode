import DisplayMode
import random
import BoomAnimation
import Option

# 单个敌人
class Alien(DisplayMode.Displayed):
    def __init__(self, start_point):
        self.active = True  # 激活状态
        self.__points = [
            start_point,
            DisplayMode.Point(start_point.x, start_point.y + 1),
            DisplayMode.Point(start_point.x, start_point.y + 2),
            DisplayMode.Point(start_point.x, start_point.y + 3),
            DisplayMode.Point(start_point.x, start_point.y + 4),

            DisplayMode.Point(start_point.x + 1, start_point.y),
            DisplayMode.Point(start_point.x + 1, start_point.y + 1),
            DisplayMode.Point(start_point.x + 1, start_point.y + 3),
            DisplayMode.Point(start_point.x + 1, start_point.y + 4),

            DisplayMode.Point(start_point.x + 2, start_point.y + 1),
            DisplayMode.Point(start_point.x + 2, start_point.y + 2),
            DisplayMode.Point(start_point.x + 2, start_point.y + 3),

            DisplayMode.Point(start_point.x + 3, start_point.y),
            DisplayMode.Point(start_point.x + 3, start_point.y + 2),
            DisplayMode.Point(start_point.x + 3, start_point.y + 4),

            DisplayMode.Point(start_point.x + 4, start_point.y),
            DisplayMode.Point(start_point.x + 4, start_point.y + 2),
            DisplayMode.Point(start_point.x + 4, start_point.y + 4)
        ]

    # 设置起始点的坐标
    def set_point(self, start_point):
        self.__points = [
            start_point,
            DisplayMode.Point(start_point.x, start_point.y + 1),
            DisplayMode.Point(start_point.x, start_point.y + 2),
            DisplayMode.Point(start_point.x, start_point.y + 3),
            DisplayMode.Point(start_point.x, start_point.y + 4),

            DisplayMode.Point(start_point.x + 1, start_point.y),
            DisplayMode.Point(start_point.x + 1, start_point.y + 1),
            DisplayMode.Point(start_point.x + 1, start_point.y + 3),
            DisplayMode.Point(start_point.x + 1, start_point.y + 4),

            DisplayMode.Point(start_point.x + 2, start_point.y + 1),
            DisplayMode.Point(start_point.x + 2, start_point.y + 2),
            DisplayMode.Point(start_point.x + 2, start_point.y + 3),

            DisplayMode.Point(start_point.x + 3, start_point.y),
            DisplayMode.Point(start_point.x + 3, start_point.y + 2),
            DisplayMode.Point(start_point.x + 3, start_point.y + 4),

            DisplayMode.Point(start_point.x + 4, start_point.y),
            DisplayMode.Point(start_point.x + 4, start_point.y + 2),
            DisplayMode.Point(start_point.x + 4, start_point.y + 4)
        ]

    # 重写父类方法，返回自己的坐标
    def get_point_list(self):
        return self.__points

    # 敌人可以降落
    def fall(self):
        for i in self.__points:
            i.x += 1
            if i.x > 46:
                self.active = False     # 超出屏幕范围，认为失效

    # 敌人被击中
    def end(self):
        center_point = self.__points[0]
        BoomAnimation.AnimationManager.manager().play(DisplayMode.Point(center_point.x + 2, center_point.y + 2))

        Option.Functions.fenshu()

        self.active = False
        self.set_point(DisplayMode.Point(-20, -20))


# 管理敌人的类
class EnemyManager(DisplayMode.Displayed):
    def __init__(self):
        self.__enemy_list = []      # 通过列表管理所有敌人
        self.__n = 0                # 记录激活状态的敌人数量

        # 总共创建8个敌人，根据激活状态，反复使用
        for i in range(8):
            alien = Alien(DisplayMode.Point(-20, -20))
            alien.active = False
            self.__enemy_list.append(alien)

    # 在失效状态的敌人里，选一个激活, 位置随机
    def create_enemy(self):
        for i in self.__enemy_list:
            if not i.active:
                i.set_point(DisplayMode.Point(-8, random.randint(0, 35)))
                i.active = True
                return

    # 让所有激活的敌人下降
    def all_fall(self):
        for i in self.__enemy_list:
            if i.active:
                i.fall()

    # 返回所有敌人的坐标，因为是直接把这个管理类添加到显示器，而不是单个敌人
    def get_point_list(self):
        all_enemy_point = []
        for i in self.__enemy_list:
            all_enemy_point += i.get_point_list()
        return all_enemy_point

    # 返回所有敌人，为了检测是否击中
    def get_enemys_list(self):
        return self.__enemy_list

    # 管理所有敌人的行为：什么时候下降，什么时候重新创建敌人
    def action(self):
        if self.__n % 2 == 0:
            self.all_fall()
        if self.__n % 20 == 0:
            self.create_enemy()
        self.__n += 1