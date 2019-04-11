import Enemys
import AirPlay
import DisplayMode

# 中弹检测，不用创建对象，直接用子弹对象和敌人对象做比较
# 所以应该创建静态方法，留下简洁的对外接口
class Injury_Check:
    @staticmethod
    def check_injury(bullet_manager: AirPlay.BulletManager, enemys: Enemys.EnemyManager):
        # 检测激活状态的子弹和敌人的坐标是否重合
        for i in bullet_manager.get_bullet_list():  # 获得所有子弹的列表
            if not i.active:
                continue
            for j in enemys.get_enemys_list():      # 获取所有敌人的列表
                if not j.active:
                    continue
                if Injury_Check.__check_interation(i.get_point_list(), j.get_point_list()):
                    i.active = False
                    i.set_point(DisplayMode.Point(-8, -8))
                    j.end()


    @staticmethod
    def __check_interation(list1, list2):
        for i in list1:
            for j in list2:
                if i.x == j.x and i.y == j.y:
                    return True
        return False
