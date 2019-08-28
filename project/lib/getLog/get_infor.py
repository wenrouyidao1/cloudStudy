
import paramiko

# 将计划任务上传至目标服务器，并执行
def updateCron(rsa_path, ip, user, cron_path, port=22):
    private = paramiko.RSAKey.from_private_key_file(rsa_path)
    transport = paramiko.Transport((ip, port))
    transport.connect(username=user, pkey=private)

    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put(localpath=cron_path, remotepath='/tmp/cron_shellScripts.sh')

    client = paramiko.SSHClient()
    client._transport = transport

    # yum -y install dos2unix（针对window和unix编码问题，windows需要提前在服务器安装好）
    client.exec_command(command='dos2unix /tmp/cron_shellScripts.sh')   # 类unix系统不需要这步

    client.exec_command(command='/usr/bin/bash /tmp/cron_shellScripts.sh')
    transport.close()


# 将shell脚本上传至目标服务器，并执行，生成日志文件
def updateShell(rsa_path, ip, user, shell_path, port=22):
    private = paramiko.RSAKey.from_private_key_file(rsa_path)
    transport = paramiko.Transport((ip, port))
    transport.connect(username=user, pkey=private)

    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.put(localpath=shell_path, remotepath='/tasks/shell_getMessage.sh')

    client = paramiko.SSHClient()
    client._transport = transport
    client.exec_command(command='dos2unix /tasks/shell_getMessage.sh')
    client.exec_command(command='/usr/bin/bash /tasks/shell_getMessage.sh')
    transport.close()


# 获取远程服务器日志文件
def getLogfile(ras_path, host, user, localpath, post=22):
    private = paramiko.RSAKey.from_private_key_file(ras_path)
    transport = paramiko.Transport((host, post))
    transport.connect(username=user, pkey=private)

    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.get(remotepath='/var/log/monitor/monitor.log', localpath=localpath)

    transport.close()


# 测试
# updateCron('C:\\Users\Administrator\.ssh\id_rsa', '192.168.43.101', 'root', 'cron_shellScripts.sh')
# updateShell('C:\\Users\Administrator\.ssh\id_rsa', '192.168.43.101', 'root', 'shell_getMessage.sh')
# getLogfile('C:\\Users\Administrator\.ssh\id_rsa', '192.168.43.101', 'root', './monitor.log')

