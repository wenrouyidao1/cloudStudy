import paramiko
private = paramiko.RSAKey.from_private_key_file('C:\\Users\Administrator\.ssh\id_rsa')

# 建立通道，并建立通道连接
transport = paramiko.Transport(('10.36.145.150', 22))
transport.connect(username='root', pkey=private)

# 建立sftp连接
sftp = paramiko.SFTPClient.from_transport(transport)

# 远程下载文件
sftp.get(remotepath='/root/onlineComputer.txt', localpath='./onlineComputer.txt')

transport.close()

# 读取ip地址文件，并按最后主机位从小到大排序
with open(file='onlineComputer.txt', mode='r', encoding='utf8') as file:
    ips, lineip = [], []
    for ip in file.readlines():
        hostip = ip.split('.')[-1].rstrip('\n')
        ips.append(int(hostip))
        ips.sort()

def continusFind(num_list):
    '''
    列表中连续数字段寻找
    '''
    s = 1
    find_list = []
    while s <= len(num_list) - 1:
        if num_list[s] - num_list[s - 1] == 1:
            flag = s - 1
            while num_list[s] - num_list[s - 1] == 1:
                s += 1
            find_list.append(num_list[flag:s])
        else:
            s += 1
    return find_list

# 将处理好的连续ip地址段分别写入文件
if __name__ == '__main__':
    s = continusFind(ips)
    for element in s:
        for hostip in element:
            with open(file='continueIp{}.txt'.format(element[0]), mode='a', encoding='utf8') as file:
                file.write('10.36.145.' + str(hostip) + '\n')


