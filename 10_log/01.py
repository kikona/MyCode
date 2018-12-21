import logging

logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log.")


# 另外一种写法
logging.log(logging.DEBUG, "This is a debug log")
logging.log(logging.INFO, "This is a debug log")
logging.log(logging.WARNING, "This is a debug log")
logging.log(logging.ERROR, "This is a debug log")
logging.log(logging.CRITICAL, "This is a debug log")

# 因为没有配置logger的输出级别，所以运行结果只有WARNING及以上的三条log