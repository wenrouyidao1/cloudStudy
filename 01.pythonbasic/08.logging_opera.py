
# 定义日志格式
# ------------------------------第一种方式-----------------------------------

import logging

# 定义日志输出的位置/级别/格式/增加规则
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(pathname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.WARNING,
    filename='./log_file/example.log',
    filemode='a'
)

# 定义触发器
# logging.fatal('this is a debug')

try:
    var01, var02 = 'hello', 18
    print(var01 + var02)
except Exception as error:
    logging.error(error)
finally:
    pass

print('go on ...')


# ------------------------------第二种方式------------------------------------

import logging.handlers

# 设置日志的记录格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(pathname)s - %(message)s')

# 以下三种格式的日志处理器三选一
# 第1种
# 设置日志处理器,将日志记录器获取的日志放到指定文件
rowHandler = logging.FileHandler(filename='./log_file/logRecording.log')

# 第2种
# 设置日志处理器,将日志记录器获取的日志放到指定文件,并根据大小进行切割
rotateHandler = logging.handlers.RotatingFileHandler(
    filename='./log_file/logRotate.log',
    maxBytes=1024 * 1024 * 5,
    backupCount=5
)

# 第3种
# 设置日志处理器,将日志记录器获取的日志文件放到指定文件,并根据时间进行切割
timeHandler = logging.handlers.TimedRotatingFileHandler(
    filename='./log_file/example.log',
    when='D',
    interval=2,
    backupCount=5
)

# 设置日志处理器处理日志的最低级别
rowHandler.setLevel(logging.WARNING)
# 为日志处理器设置格式化器
rowHandler.setFormatter(formatter)

# 设置日志的记录器,默认记录器的名字为root
logger = logging.getLogger()
# 设置日志记录器的最低记录级别
logger.setLevel(logging.WARNING)
# 为日志记录器添加处理器
logger.addHandler(rowHandler)


try:
    var01, var02 = 'hello', 18
    print(var01 + var02)
except Exception as error:
    logger.error(error)
finally:
    pass

print('go on ...')


# -----------------------------第三种方式(写配置文件，推荐使用)--------------------------------

import logging.config

# 指定日志格式的配置文件位置
logging.config.fileConfig('./cnf/logging.conf')

try:
    var01, var02 = 'hello', 20
    print(var01 + var02)
except Exception as error:
    logger = logging.getLogger()   # 该参数为日志格式中的name，不写默认为root
    logger.error(error)
finally:
    pass

print('go on...')
