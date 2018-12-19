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
            - 格式：level:log_name:content
