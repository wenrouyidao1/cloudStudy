
class Logfile:
    def __init__(self, path):
        self.path = path

    # 统计一个网站的PV量和UV量
    def count_ip(self):
        ips = []
        with open(self.path, 'r', encoding='utf8') as file:
            for lines in file:
                ips.append(lines.split()[0])
            PV = len(ips)
            UV = len(set(ips))
        return PV, UV

    # 统计一个网站前十名ip信息
    def get_ip(self):
        ips = {}
        with open(self.path, 'r', encoding='utf8') as file:
            for lines in file:
                ips.setdefault(lines.split()[0], 0)
                ips[lines.split()[0]] += 1
            listA = sorted(ips.items(), key=lambda x: x[1], reverse=True)
            ips = dict(listA[0:10])
        return ips

    # 统计日志中200、302、303、304、400、404、499、502、503、504状态码出现的次数
    def getStatusCode(self):
        statusCode = {}
        with open(self.path, 'r', encoding='utf8') as file:
            for lines in file:
                key = lines.split()[8]
                if key in ('200', '302', '303', '304', '400', '404', '499', '502', '503', '504'):
                    statusCode.setdefault(key, 0)
                    statusCode[key] += 1
                listA = sorted(statusCode.items(), key=lambda x: x[1], reverse=True)
                statusCode = dict(listA)
        return statusCode

    # 统计日志中最热的资源
    def hotNatural(self):
        natural = {}
        with open(self.path, 'r', encoding='utf8') as file:
            for lines in file:
                key = lines.split()[6]
                natural.setdefault(key, 0)
                natural[key] += 1
            listB = sorted(natural.items(), key=lambda x: x[1], reverse=True)
            natural = dict(listB[0:10])
        return natural

# 实例化
getData = Logfile('./log_file/access_log')
