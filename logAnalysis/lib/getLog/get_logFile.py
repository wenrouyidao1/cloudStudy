
import paramiko


# 获取远程服务器上的日志文件, 到本地
def get_logFile(rsa_path, ip, user, local_path, port=22):
    private = paramiko.RSAKey.from_private_key_file(rsa_path)
    transport = paramiko.Transport((ip, port))
    transport.connect(username=user, pkey=private)

    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.get(remotepath='/var/log/access/access.log', localpath=local_path)

    transport.close()


# 获取远程主机主机名
def get_hostname(rsa_path, ip, user, port=22):
    private = paramiko.RSAKey.from_private_key_file(rsa_path)
    transport = paramiko.Transport((ip, port))
    transport.connect(username=user, pkey=private)
    clientA = paramiko.SSHClient()
    clientA._transport = transport

    _, stdout, _ = clientA.exec_command('hostname')
    Hostname = stdout.read().decode('utf-8')

    transport.close()
    return Hostname


# 测试
# get_logFile('C:\\Users\Administrator\.ssh\id_rsa', '192.168.43.101', 'root', '../logFile/access.log')

