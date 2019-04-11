import time
import DisplayMode
import AirPlay
import Enemys
import InjuryCheck
import BoomAnimation
import threading
import msvcrt

# 开线程，检测键盘按键输入
class ControlThread(threading.Thread):
    def run(self):
        while True:
            time.sleep(0.05)
            global jet
            c = str(msvcrt.getch())  # 输入函数，不需要敲回车，但是值为: b'x'
            if c == "b'a'":  # 不输入的话，就会卡在这里等，但是不影响主线程
                jet.move_left()
            elif c == "b'd'":
                jet.move_right()
            if c == "b'j'":
                # 开火
                bullet_manager.create_bullet()
            elif c == "b'q'":
                global running
                running = False
                exit(0)  # 退出当前线程

# 创建显示器
display = DisplayMode.Displayer()

# 创建飞机
jet = AirPlay.airplay()
# 创建敌人
enemys = Enemys.EnemyManager()
# 创建子弹
bullet_manager = AirPlay.BulletManager(jet)

# 把飞机添加到显示器
display.add_item(jet)
# 把所有敌人添加到显示器
display.add_item(enemys)
# 把所有子弹添加到显示器
display.add_item(bullet_manager)
# 把图案添加到显示器
display.add_item(BoomAnimation.AnimationManager.manager())


running = True  # 程序运行标志

# 启动线程
control = ControlThread()
control.start()

while running:
    enemys.action()
    bullet_manager.action()

    InjuryCheck.Injury_Check.check_injury(bullet_manager, enemys)
    BoomAnimation.AnimationManager.manager().action()

    display.reflash()
    time.sleep(0.1)
