
from redis import sentinel
import logging.config
import redis

# 指定日志格式的配置文件位置
logging.config.fileConfig('./cnf/logging.conf')
# 连接哨兵
stinel = sentinel.Sentinel([('192.168.43.100', 26379)])


# ------------------1.测试方式一----------------------------------------------------
if stinel.discover_master('mymaster') != ('192.168.43.100', 6380):
    logging.getLogger('rotate')
    logging.warning('！！！master is on {}'.format(stinel.discover_master('mymaster')))
else:
    print('now master is on {}'.format(stinel.discover_master('mymaster')))


# -------------------2.测试方式二-----------------------------------------------------

# 捕捉异常，当主机刚宕机，从机正在选票时会发送错误：找不到主机
try:
    master = stinel.discover_master('mymaster')
    print(master)
except redis.sentinel.MasterNotFoundError as error:
    logging.getLogger('rotate')
    logging.error(error)
    # 采用钉钉报警的方式通知运维人员dingtalk(error)
finally:
    master = stinel.discover_master('mymaster')
    if master != ('192.168.43.100', 6380):
        logging.warning('！！！master on {}'.format(master))
