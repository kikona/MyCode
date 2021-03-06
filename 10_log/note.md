# LOG
- https://www.cnblogs.com/yyds/p/6901864.html
- logging
- logging模块：提供模块级别的函数记录日志，本身还包括四大组件

## 日志相关的概念
- 日志
- 日志的级别（level）
    - 不同的用户关注不同的程序信息，以下级别从低到高
    - debug
    - info（信息知）
    - notice（通知）
    - warning（警告）
    - error
    - critical（危急）
    - alert（警报）
    - emergency（紧急事件）
- 打印出日志其实是一种IO操作，它的速度很慢，不要频繁的进行IO操作
- LOG的作用
    - 调试
    - 了解软件的运行情况
    - 分析定位问题
- 日志信息，需要有以下几个方面：
    - 时间
    - 地点
    - 级别
    - 内容，要求言简意赅
- 成熟的第三方日志：
    - log4j
    - log4php
    - logging

# Logging模块
- 日志级别:级别可以定义
    - DEBUG
    - INFO
    - WARNING
    - ERROR
    - CRITICAL
    - 到最后两个级别的时候，程序基本就不行了
- 初始化或许写日志实例的时候，需要指定级别，只有当级别等于或高于指定级别的时候，才被记录
- 使用方式
    - 直接使用logging（封装了其他组件）
    - Logging四大组件
    
# logging模块级别的日志
- 使用以下几个函数
    - logging.debug(msg, *args, **kwargs)   创建一条严重级别为DEBUG的日志记录
    - logging.info(msg, *args, **kwargs)    创建一条严重级别为INFO的日志记录
    - logging.warning(msg, *args, **kwargs) 创建一条严重级别为WARNING的日志记录
    - logging.error(msg, *args, **kwargs)   创建一条严重级别为ERROR的日志记录
    - logging.critical(msg, *args, **kwargs)创建一条严重级别为CRITICAL的日志记录
    - logging.log(level, *args, **kwargs)   创建一条严重级别为level的日志记录
        - level由用户自定义，log可以替代前面5个函数，用法都差不多
    - logging.basicConfig(**kwargs)         对root logger进行一次性配置
        - 只在第一次调用的时候起作用
        - 不配置logger，则使用默认值
            - 输出位置：sys.stderr
            - 级别：WARNING
            - 日志的格式：level:log_name:content
        - 配置格式：
            - level=logging.等级名：修改输出的等级
            - filename="绝对路径或者文件名"
                - 表示日志输出保存在指定的文件中
                - 只写文件名时，表明文件创建在当前目录下
            - format=自定义格式名
                - 首先要自定义格式：格式名 = "格式具体形式，含参数名"
                - 然后使用format=自定义格式名，就能更改日志格式
                - 参数：
                    
                    
                        asctime	%(asctime)s	日志事件发生的时间--人类可读时间，如：2003-07-08 16:49:45,896
                        created	%(created)f	日志事件发生的时间--时间戳，就是当时调用time.time()函数返回的值
                        relativeCreated	%(relativeCreated)d	日志事件发生的时间相对于logging模块加载时间的相对毫秒数（目前还不知道干嘛用的）
                        msecs	%(msecs)d	日志事件发生事件的毫秒部分
                        levelname	%(levelname)s	该日志记录的文字形式的日志级别（'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'）
                        levelno	%(levelno)s	该日志记录的数字形式的日志级别（10, 20, 30, 40, 50）
                        name	%(name)s	所使用的日志器名称，默认是'root'，因为默认使用的是 rootLogger
                        message	%(message)s	日志记录的文本内容，通过 msg % args计算得到的
                        pathname	%(pathname)s	调用日志记录函数的源码文件的全路径
                        filename	%(filename)s	pathname的文件名部分，包含文件后缀
                        module	%(module)s	filename的名称部分，不包含后缀
                        lineno	%(lineno)d	调用日志记录函数的源代码所在的行号
                        funcName	%(funcName)s	调用日志记录函数的函数名
                        process	%(process)d	进程ID
                        processName	%(processName)s	进程名称，Python 3.1新增
                        thread	%(thread)d	线程ID
                        threadName	%(thread)s	线程名称
    
   - 案例 01
   
# logging模块的处理流程
- 四大组件及其相关的类：
     - 日志器（Logger）：产生日志的一个接口
     - 处理器（Handler）：把产生的日志发送到相应的目的地
     - 过滤器（Filter）：更精细的控制哪些日志输出
     - 格式（Formatter）：对输出的信息格式化
- Logger类：产生一个日志
    - 拥有的操作：
        - Logger.setLevel()	设置日志器将会处理的日志消息的最低严重级别
        - Logger.addHandler() 和 Logger.removeHandler()	为该logger对象添加 和 移除一个handler对象
        - Logger.addFilter() 和 Logger.removeFilter()	为该logger对象添加 和 移除一个filter对象
        - 产生一个与它们的方法名对应等级的日志：
            - Logger.debug(),Logger.info(), Logger.warning(), Logger.error(), Logger.critical()	
        - Logger.exception()	创建一个类似于Logger.error()的日志消息
        - Logger.log()	需要获取一个明确的日志level参数来创建一个日志记录
    - 如何得到一个logger对象
        - 方法一：实例化，但是一般不推荐，因为只能有一个日志，一个人记录就可以了
        - 方法二：logging.getLogger()
        
- Handler类：把log发送到指定位置
    - 方法：
        - Handler.setLevel()	设置handler将会处理的日志消息的最低严重级别
        - Handler.setFormatter()	为handler设置一个格式器对象
        - Handler.addFilter() 和 Handler.removeFilter()	为handler添加 和 删除一个过滤器对象
    - 不需要直接只用，Handler是基类，它只定义了素有handlers都应该有的接口，同时提供了一些子类可以直接使用或覆盖的默认行为。
    - 常用的Handler子类：
        - logging.StreamHandler	将日志消息发送到输出到Stream，如std.out, std.err或任何file-like对象。
        - logging.FileHandler	将日志消息发送到磁盘文件，默认情况下文件大小会无限增长
        - logging.handlers.RotatingFileHandler	将日志消息发送到磁盘文件，并支持日志文件按大小切割
        - logging.hanlders.TimedRotatingFileHandler	将日志消息发送到磁盘文件，并支持日志文件按时间切割
        - logging.handlers.HTTPHandler	将日志消息以GET或POST的方式发送给一个HTTP服务器
        - logging.handlers.SMTPHandler	将日志消息发送给一个指定的email地址
        - logging.NullHandler	该Handler实例会忽略error messages，通常被想使用logging的library开发者使用来
          避免'No handlers could be found for logger XXX'信息的出现。
          
- Format类：配置日志信息的最终顺序、结构和内容
    - 可以直接实例化使用
    - 也可以继承Format添加特殊的内容
    - 三个参数：
        - fmt：指定消息格式化字符串，如果不指定该参数则默认使用message的原始值
        - datefmt：指定日期格式字符串，如果不指定该参数则默认使用"%Y-%m-%d %H:%M:%S"
        - style：可取值为 '%', '{'和 '$'，如果不指定该参数则默认使用'%'
        
- Filter类：控制传递过来的信息的具体内容
    - 可以被Handler和Logger用来做比level更细腻的、更复杂的过滤功能
    - Filter是一个过滤器基类，它只允许某个logger层级下的日志事件通过过滤
 - 案例02
