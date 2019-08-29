
import pymysql
import paramiko
from getLog import get_logFile


# 对所收集的日志文件进行分析, 提取pv/uv量; 排名前10的IP地址; 状态码分布情况;
# 统计一个网站的PV量和UV量
def count_ip(path):
    ips = []
    with open(path, 'r', encoding='utf8') as file:
        for lines in file:
            ips.append(lines.split()[0])
        PV = len(ips)
        UV = len(set(ips))
    return PV, UV

# 统计一个网站前十名ip信息
def get_ip(path):
    ips = {}
    with open(path, 'r', encoding='utf8') as file:
        for lines in file:
            ips.setdefault(lines.split()[0], 0)
            ips[lines.split()[0]] += 1
        listA = sorted(ips.items(), key=lambda x: x[1], reverse=True)
        ips = dict(listA[0:10])
    return ips

# 统计日志中200、302、303、304、400、404、499、502、503、504状态码出现的次数
def getStatusCode(path):
    statusCode = {}
    with open(path, 'r', encoding='utf8') as file:
        for lines in file:
            key = lines.split()[8]
            if key in ('200', '302', '303', '304', '400', '404', '499', '502', '503', '504'):
                statusCode.setdefault(key, 0)
                statusCode[key] += 1
            listA = sorted(statusCode.items(), key=lambda x: x[1], reverse=True)
            statusCode = dict(listA)
    return statusCode

# 统计日志中最热的资源
def hotNatural(path):
    natural = {}
    with open(path, 'r', encoding='utf8') as file:
        for lines in file:
            key = lines.split()[6]
            natural.setdefault(key, 0)
            natural[key] += 1
        listB = sorted(natural.items(), key=lambda x: x[1], reverse=True)
        natural = dict(listB[0:10])
    return natural


# 处理得到的日志，并记入到数据库
def insert_database(host, user, password, db, rsa_path, log_path, hostname_ip, port=3306):
    client = pymysql.connect(host=host, port=port, user=user, password=password, db=db, charset='utf8')
    cursors = client.cursor()

    Hostname = get_logFile.get_hostname(rsa_path, hostname_ip, 'root')

    for element in ['puv', 'ips', 'code']:
        if element == 'puv':
            pv, uv = count_ip(log_path)
            sql = "insert into element values('{}', {}, {});"
            cursors.execute(sql.format(Hostname, pv, uv))
        elif element == 'ips':
            ips, listA = get_ip(log_path), []
            for ip in ips.keys():
                listA.append(ip)
            sql = "insert into element values('{}', '{}', '{}');"
            cursors.execute(sql.format(Hostname, listA[0], listA[1]))
        elif element == 'code':
            codes, listB = getStatusCode(log_path), []
            for code in codes.values():
                listB.append(code)
            sql = "insert into element values('{}', {}, {});"
            cursors.execute(sql.format(Hostname, listB[0], listB[1]))


    client.commit()
    client.close()



# 测试
# codes = getStatusCode('../logFile/access.log')
# print(codes.keys())
# insert_database('192.168.43.102', 'Harper', '(Harper..0822)', 'webInfo',
#                 'C:\\Users\Administrator\.ssh\id_rsa', '../logFile/access.log', '192.168.43.101')

