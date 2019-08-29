
from lib.getLog import get_logFile
from lib.log_analysis import deal_logFile


# 1. 获取远程服务器日志文件, 到本地
get_logFile.get_logFile('C:\\Users\Administrator\.ssh\id_rsa', '192.168.43.101', 'root',
                        '../logFile/access.log')


# 2. 对所收集的日志文件进行分析, 提取pv/uv量; 排名前10的IP地址; 状态码分布情况;
# 统计一个网站的PV量和UV量
pv, uv = deal_logFile.count_ip('../logFile/access.log')
print(pv, uv)

# 统计一个网站前十名ip信息
ips = deal_logFile.get_ip('../logFile/access.log')
print(ips)

# 统计日志中200、302、303、304、400、404、499、502、503、504状态码出现的次数
codes = deal_logFile.getStatusCode('../logFile/access.log')
print(codes)

# 统计日志中最热的资源
source = deal_logFile.hotNatural('../logFile/access.log')
print(source)


# 3. 处理得到的日志，并记入到数据库
deal_logFile.insert_database('192.168.43.102', 'Harper', '(Harper..0822)', 'webInfo',
                'C:\\Users\Administrator\.ssh\id_rsa', '../logFile/access.log', '192.168.43.101')

