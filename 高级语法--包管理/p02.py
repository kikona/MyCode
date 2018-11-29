# 调用模块p01
# import p01 就相当于把p01的所有内容，粘贴到p02的最前面
# 所以 print("这是模块p01") 这一句会最先运行

import p01

stu = p01.Student("xioajing", 19)

stu.say()

p01.sayhello()
