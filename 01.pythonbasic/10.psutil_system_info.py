
import psutil
import json
import time

# ----------------------------------cpu_Information---------------------------------------

# user / (system + stop) / io / idle
# 所有进程占用cpu的总时间
cpu = psutil.cpu_times()
print(cpu)

# 检测CPU被各个进程占用的时间 百分比
cpuInfo = psutil.cpu_times_percent(interval=1)              # 参数为时间间隔1秒
print('user process percent: {}'.format(cpuInfo.user))      # 执行用户进程的时间百分比
print('system process percent: {}'.format(cpuInfo.system))  # 执行内核进程和中断的时间百分比
print('iowait process percent: {}'.format(cpuInfo.iowait))  # 由于IO等待而使CPU处于idle(空闲)状态的时间百分比
print('idle process percent: {}'.format(cpuInfo.idle))      # CPU处于idle状态的时间百分比

# 后端生产数据([python]Django) -->> (VUE/React[JavaScript]-[json])前端消费数据: 显示到页面中(给用户(运维)看)
# [{20190820162004: {user: None, system: None, iowait: None, idle: None}}]


def data():
    cpuInfo = psutil.cpu_times_percent(interval=1)
    date = time.strftime('%Y%m%d%H%M%S', time.localtime())   # 定义时间显示格式
    module = [{date: {'user': cpuInfo.user, 'system': cpuInfo.system, 'iowait': cpuInfo.iowait, 'idle': cpuInfo.idle}}]
    return module

# 记录十秒内cpu变化情况
source = []
for bout in range(10):
    source.extend(data())
result = json.dumps(source)
print(result)
print(type(result))


# ------------------------------------memory_information-----------------------------------

# 获取完整的物理内存信息
memInfo = psutil.virtual_memory()
print(memInfo.total)    # 1024*1024*1024 bit = 1024*1024 KBit = 1024 MBit = 1 GBit
print('{:.0f}M'.format(memInfo.total/1024/1024))     # 内存总数
print('{:.0f}M'.format(memInfo.used/1024/1024))      # 已使用的内存数
print('{:.0f}M'.format(memInfo.free/1024/1024))      # 空闲内存数
print('{:.0f}M'.format(memInfo.buffers/1024/1024))   # 缓冲使用数
print('{:.0f}M'.format(memInfo.cached/1024/1024))    # 缓存使用数

# 获取完整的虚拟内存信息
swapInfo = psutil.swap_memory()
print(swapInfo)


# -----------------------------------disk_information----------------------------------------

diskInfo = psutil.disk_partitions()        # 获取磁盘整体情况
print(diskInfo)
diskInfo = psutil.disk_io_counters()       # 获取硬盘总的IO个数和读写信息
print(diskInfo)
diskInfo = psutil.disk_usage('/')          # 获取指定分区的使用情况(常用)
print(diskInfo.total, diskInfo.used, diskInfo.free)



# 生成CPU/Memory/Disk的信息模板
monitorInfo = [{'date': {
    'cpu': {'user': None, 'system': None, 'iowait': None, 'idle': None},
    'memory': {'total': None, 'used': None, 'free': None, 'buffer': None, 'Cached': None},
    'disk': {'total': None, 'used': None, 'free': None}
}}]


# ------------------------------------network_information------------------------------------

networkInfo = psutil.net_io_counters()      # 获取网络信息
print(networkInfo)
