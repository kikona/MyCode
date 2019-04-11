import DisplayMode

# 单个动画类
class Animation(DisplayMode.Displayed):
    def __init__(self):
        self.__first = []
        self.__second = []
        self.active = True
        self.step = 0

    # 动画的坐标由敌人的位置确定，所以不用初始化，拥有设定坐标的函数即可
    def set_point(self, center_point):
        self.__first = [
            DisplayMode.Point(center_point.x - 2, center_point.y - 2),
            DisplayMode.Point(center_point.x - 2, center_point.y + 2),
            DisplayMode.Point(center_point.x + 2, center_point.y - 2),
            DisplayMode.Point(center_point.x + 2, center_point.y + 2),
            DisplayMode.Point(center_point.x - 1, center_point.y - 1),
            DisplayMode.Point(center_point.x - 1, center_point.y + 1),
            DisplayMode.Point(center_point.x + 1, center_point.y - 1),
            DisplayMode.Point(center_point.x + 1, center_point.y + 1)
        ]

        self.__second = [
            DisplayMode.Point(center_point.x - 2, center_point.y - 2),
            DisplayMode.Point(center_point.x - 2, center_point.y + 2),
            DisplayMode.Point(center_point.x + 2, center_point.y - 2),
            DisplayMode.Point(center_point.x + 2, center_point.y + 2),
            DisplayMode.Point(center_point.x - 1, center_point.y - 1),
            DisplayMode.Point(center_point.x - 1, center_point.y + 1),
            DisplayMode.Point(center_point.x + 1, center_point.y - 1),
            DisplayMode.Point(center_point.x + 1, center_point.y + 1),

            center_point,

            DisplayMode.Point(center_point.x - 2, center_point.y - 1),
            DisplayMode.Point(center_point.x - 1, center_point.y + 2),
            DisplayMode.Point(center_point.x + 1, center_point.y - 2),
            DisplayMode.Point(center_point.x + 2, center_point.y + 1)

        ]

    # 播放初始化
    def play(self):
        self.step = 0
        self.active = True

    # 播放步骤设定，播放步骤改变，从而改变播放图案
    def run(self):
        self.step += 1
        if self.step == 3:
            self.active = False

    # 返回图案坐标，根据要显示的某个图案，返回对应的坐标
    def get_point_list(self):
        d = {
            # 0: self.__first,
            1: self.__second,
            2: self.__first
        }
        # 还要检测是否是激活状态，失效状态时就不用返回图案坐标了
        if self.active:
            return d[self.step]
        else:
            return []

# 创建类外的单例对象
animation_manager = None

# 管理动画
class AnimationManager(DisplayMode.Displayed):
    def __init__(self):
        self.__animations_list = []

        # 创建和敌人数量一样多的图案
        for i in range(8):
            animation = Animation()
            self.__animations_list.append(animation)

    # 获取单例对象, 这样的话，在程序任何地方都可以用了类名调用animation_manager
    @staticmethod
    def manager():
        global animation_manager
        if not animation_manager:
            animation_manager = AnimationManager()
        return animation_manager        # 返回的是一个单例对象

    # 找到一个失效状态的动画播放，要给显示位置
    def play(self, center_point):
        for i in self.__animations_list:
            if not i.active:
                i.set_point(center_point)
                i.play()

    # 播放所有激活状态的动画
    def run(self):
        for i in self.__animations_list:
            if i.active:
                i.run()

    # 返回所有动画的坐标
    def get_point_list(self):
        list_point = []
        for i in self.__animations_list:
            list_point += i.get_point_list()
        return list_point

    # main函数调用接口
    def action(self):
        self.run()


