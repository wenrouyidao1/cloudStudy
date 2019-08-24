
import redis
import logging.config


# 指定日志格式的配置文件位置
logging.config.fileConfig('./cnf/logging.conf')

# 创建redis连接池和建立连接客户端
pool = redis.ConnectionPool(host='192.168.43.100', port=6379, db=0)
client = redis.Redis(connection_pool=pool)

# 实验之前先创建hash表
client.hmset(name='chenguoqi', mapping={'age': 18, 'sex': 'man', 'tall': '180cm'})

# 指定要删除的表中的键【规范为：chenguoqi age sex ...】
hashMap = input('please input table and keys:')

# 捕捉异常，当用户输入的字符串不符合规范时会报错
try:
    mapping = hashMap.split()
    for index in range(1, len(mapping)):
        # 可用if判断要留下的键值
        client.hdel(mapping[0], mapping[index])
except Exception as error:
    logging.getLogger('rotate')
    logging.error(error)
finally:
    print('Cached clear complete!')

# 检查是否删除成功
print(client.hmget('chenguoqi', 'age', 'sex', 'tall'))

# ------------------------------------------------------------------
# 清除当前所指定的数据库(缓存位置)内的数据 - redis.conf里面记录的database number:16
client.flushdb(16-1)

# 清除所有的数据(不分位置)
client.flushall()
