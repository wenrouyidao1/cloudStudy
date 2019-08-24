
# 建立远程连接主机，远程连接/上传下载
import paramiko

# -----------------------------------1. 密码连接--------------------------------------

# 建立客户端
client = paramiko.SSHClient()

# 添加指纹
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 建立连接
client.connect(
    hostname='10.36.145.120',
    port=22,
    username='root',
    password='1'
)

# 执行的任务
stdin, stdout, stderr = client.exec_command(command='cat /etc/passwd', timeout=1)
print(stdout.read().decode('utf-8'))

# 一定要关闭客户端连接
client.close()


# -----------------------------------2. 密钥连接-----------------------------------------

# 前提：先在本机创建密钥对（ssh-keygen），并把公钥传到目标主机（ssh-copy-id）

# 指定本机的私钥路径
private = paramiko.RSAKey.from_private_key_file('C:\\Users\Administrator\.ssh\id_rsa')

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(
    hostname='10.36.145.120',
    port=22,
    username='root',
    pkey=private
)

stdin, stdout, stderr = client.exec_command(command='cat /etc/shadow', timeout=1)
print(stdout.read().decode('utf-8'))
print(stderr.read().decode('utf-8'))

client.close()

# -------------------------------------3. 通道连接-----------------------------------

# 前提：先在本机创建密钥对（ssh-keygen），并把公钥传到目标主机（ssh-copy-id）

# 指定本机的私钥路径
private = paramiko.RSAKey.from_private_key_file('C:\\Users\Administrator\.ssh\id_rsa')

# 建立通道
transport = paramiko.Transport(('10.36.145.120', 22))

# 建立通道连接
transport.connect(username='root', pkey=private)

# 创建客户端，并指定使用通道连接
client = paramiko.SSHClient()
client._transport = transport

stdin, stdout, stderr = client.exec_command('cat /etc/group', timeout=1)
print(stdout.read().decode('utf-8'))
print(stderr.read().decode('utf-8'))

# 关闭通道
transport.close()

# ------------------------------------4. 通道传输文件-------------------------------

# 前提：先在本机创建密钥对（ssh-keygen），并把公钥传到目标主机（ssh-copy-id）

# 指定本机的私钥路径
private = paramiko.RSAKey.from_private_key_file('C:\\Users\Administrator\.ssh\id_rsa')

# 建立通道，并建立通道连接
transport = paramiko.Transport(('10.36.145.120', 22))
transport.connect(username='root', pkey=private)

# 建立sftp连接
sftp = paramiko.SFTPClient.from_transport(transport)

# 远程上传/下载文件
sftp.get(remotepath='/root/cpu_access.log', localpath='./txt_file/cpuAccess.txt')
sftp.put(localpath='./txt_file/cpuAccess.txt', remotepath='/mnt/cpu_access.txt')

transport.close()
