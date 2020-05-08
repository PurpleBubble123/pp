# It is a nice day. Let's get start
# @Author : Boya
# @Time   : 03/05/2020 13.42

import logging

##############################
# 1. debug 调试级别的日志
# 2. info  信息级别的日志
# 3. warning  警告级别的日志
# 4. error  错误级别的日志
##############################

##############################
# eg.1
# logging.basicConfig(level=logging.DEBUG)
# logging.debug("This is a debug log")
# logging.info("This is a info log")
# logging.warning("This is a warning log")
# logging.error("This is a error log")


####################################
# eg.2 生成log文件 及规定格式
# LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
# DATE_FORMAT = "%Y/%m/%d %H:%M:%S"
#
# logging.basicConfig(filename="my.log", level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)
# logging.debug("This is a debug log")
# logging.info("This is a info log")
# logging.warning("This is a warning log")
# logging.error("This is a error log")


####################################
# eg.3

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%Y/%m/%d %H:%M:%S"

logger = logging.getLogger()
logger.setLevel("DEBUG")

# 文件处理器，输出到文件
file_handler = logging.FileHandler("all.log",encoding="UTF-8")
# 流处理器，控制输出到控制台
steam_handler = logging.StreamHandler()

# 错误日志单独输出到一个文件中
error_handler = logging.FileHandler("error.log",encoding="UTF-8")
error_handler.setLevel(logging.ERROR)

# 将所有的处理器添加到logger中
logger.addHandler(file_handler)
logger.addHandler(steam_handler)
logger.addHandler(error_handler)

# 格式化
formatter = logging.Formatter(fmt="%(asctime)s - %(levelname)s - %(message)s",datefmt = "%Y/%m/%d %H:%M:%S")

# 设置格式化器，需要针对每一个处理器分别设置
file_handler.setFormatter(formatter)
steam_handler.setFormatter(formatter)
error_handler.setFormatter(formatter)

# 过滤器
my_filter = logging.Filter("打印")
file_filer_log = file_handler.addFilter(my_filter)


logger.info("日志打印")
logger.error("错误日志")


