
import redis

# 创建连接池
pool = redis.ConnectionPool(host='192.168.43.100', port=6379, db=0)
# 建立连接客户端
client = redis.Redis(connection_pool=pool)

# ----------------------------string--------------------------------

# 向redis数据库添加数据(当所设置键存在时则进行修改, 若键不存在时则添加)
client.set(name='chenguoqi', value='180')

# 向redis数据库批量添加数据
client.mset(mapping={'user': 'Harper', 'password': '123456', 'ipAddress': '192.168.43.100'})

# 获取redis数据库中的数据
result = str(client.get(name='chenguoqi'), 'utf8')
print(result)

result = client.mget('user', 'ipAddress')
print(result)

# string删除
client.delete('chenguoqi', 'user', 'password')
print(client.get('ipAddress'), client.get('user'))


# ---------------------------hash------------------------------------

# hash添加数据
client.hset(name='chenguoqi', key='age', value='18')
result = str(client.hget(name='chenguoqi', key='age'), 'utf8')
print(result)

# hash批量添加数据
client.hmset(name='wenzhisheng', mapping={'age': 38, 'sex': 'women', 'length': '5cm'})
result = client.hmget(name='wenzhisheng', keys=('age', 'sex', 'length'))
print(result)

# hash删除数据
client.hdel('wenzhisheng', 'age', 'sex')
print(client.hget('wenzhisheng', 'age'))
print(client.hget('wenzhisheng', 'length'))

# delete既可删除hash表，也可删除某个键
# client.delete('wenzhisheng', 'length')
# result = client.hget('wenzhisheng', 'length')
# print(result)

# 获取hash所有键
keys = client.hkeys('wenzhisheng')
print(keys)

# 获取hash所有值
vals = client.hvals('wenzhisheng')
print(vals)

# 获取hash所有的键-值对
items = client.hgetall('wenzhisheng')
print(items)

# 查看hash内部是否含有某个键-值对
if client.hexists('wenzhisheng', 'length'):
    print('True')
else:
    print('False')


# --------------------------------list-----------------------------

# 列表类型的增加和删除操作
client.delete('number01')
client.delete('number02')

# 从列表的左边添加
client.lpush('number01', 1, 2, 3, 4, 5)
result = client.lrange(name='number01', start=0, end=-1)
print(result)

# 从列表的右边添加
client.rpush('number02', 5, 4, 3, 2, 1)
result = client.lrange(name='number02', start=0, end=-1)
print(result)

# 列表存在时，从列表的lpushx（左）， rpushx（右）添加；若列表不存在，则不添加，输出为空
client.lpushx(name='number01', value='lpushx')
result = client.lrange(name='number01', start=0, end=-1)
print(result)
client.rpushx(name='number01', value='rpushx')
result = client.lrange(name='number01', start=0, end=-1)
print(result)

# 列表指定元素（refvalue）的相对位置（where）插入数据（value）【BEFORE：在指定元素前；AFTER：在指定元素后】
client.linsert(name='number01', where='BEFORE', refvalue=3, value='linsert')
print(client.lrange(name='number01', start=0, end=-1))

# 列表修改
client.lset(name='number01', index=4, value='lset')
print(client.lrange(name='number01', start=0, end=-1))

# 列表按索引查找
data = client.lindex(name='number01', index=0)
print(data)

# 列表删除数据【lrem：删除多少个（count）数据（value）】【ltrim：删除指定范围外的数据】
client.lpushx(name='number01', value=5)
client.lrem(name='number01', count=2, value=5)
print(client.lrange(name='number01', start=0, end=-1))

client.ltrim(name='number01', start=-3, end=-2)
print(client.lrange(name='number01', start=0, end=-1))


# -------------------------------set（无序的）--------------------------------------

# 集合增加数据
client.sadd('Set', 1, 4, 3, 2, 5)

# 集合查找数据
data = client.smembers('Set')
print(data)

# 集合删除数据（因为是无序的，所以随机删除，不建议使用）
client.spop(name='Set')
data = client.smembers('Set')
print(data)
