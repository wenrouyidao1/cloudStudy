
from lib.getLog import get_info
from lib.logAnalysis import deal_log


# 1. 将计划任务脚本上传至服务器， 并执行
get_info.updateCron('C:\\Users\Administrator\.ssh\id_rsa', '192.168.43.101', 'root',
                    './lib/getLog/cron_shellScripts.sh')

# 2. 将shell脚本上传至目标服务器，并执行，生成日志文件
get_info.updateShell('C:\\Users\Administrator\.ssh\id_rsa', '192.168.43.101', 'root',
                     './lib/getLog/shell_getMessage.sh')

# 3. 拉取远程服务器上的日志文件
get_info.getLogfile('C:\\Users\Administrator\.ssh\id_rsa', '192.168.43.101',
                    './lib/logFile/monitor.log')

# 4. 处理得到的日志文件，进行日志记录（报警信息）
deal_log.dealLog('./lib/logFile/monitor.log')

# 5.1 处理得到的日志文件，进行钉钉报警
deal_log.dingtalk('29d923806d11a9f1836b51c8882e94cda74eded55ccd2aeac9ffa98523e14af0',
                  './lib/logFile/monitor.log')

# 5.2 处理得到的日志文件，进行邮件报警
deal_log.send_mail('./lib/logFile/monitor.log', '2914283700@qq.com', 'wxuitofvcejydebj')

# 6. 处理得到的日志文件，写入数据库
deal_log.insert_database('./lib/logFile/monitor.log', '192.168.43.102', 'Harper',
                         '(Harper..0822)', 'systemInfo')
