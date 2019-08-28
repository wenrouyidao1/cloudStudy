
import json
import pymysql
import logging.config
import requests
import yagmail


# 处理得到的日志文件，进行日志记录（报警信息）
def dealLog(log_path, cpu=85, memory=90, disk=90):
    logging.config.fileConfig('../cnf/logging.conf')
    logger = logging.getLogger('rotate')

    with open(file=log_path, mode='r', encoding='utf8') as file:
        for lines in file.readlines():
            data = json.loads(lines.split('-')[-1])
            for item in data.items():
                if item[0] == 'cpu':
                    if item[1]['user'] + item[1]['system'] > cpu:
                        logger.warning('！！！cpu useRate: {}'.format(item[1]['user'] + item[1]['system']))
                elif item[0] == 'memory':
                    if item[1]['useRate'] > memory:
                        logger.warning('！！！memory useRate: {:.2f}'.format(item[1]['useRate']))
                elif item[0] == 'disk':
                    if item[1]['useRate'] > disk:
                        logger.warning('！！！disk useRate: {}'.format(item[1]['useRate']))



# 处理得到的日志文件，进行钉钉报警
def dingtalk(token, log_path, cpu=85, memory=90, disk=90):
    api = "https://oapi.dingtalk.com/robot/send?access_token={}".format(token)
    header = {'Content-Type': 'application/json'}

    def information(message, phone):
        data = {"msgtype": "text", "text": {"content": "{}".format(message)}, "at": {"atMobiles": ["{}".format(phone)], "isAtAll": False}}
        sendMessage = json.dumps(data).encode('utf-8')
        return sendMessage

    with open(file=log_path, mode='r', encoding='utf8') as file:
        for lines in file.readlines():
            data = json.loads(lines.split('-')[-1])
            for item in data.items():
                if item[0] == 'cpu':
                    if item[1]['user'] + item[1]['system'] > cpu:
                        requests.post(url=api, data=information(
                            message='[warning] cpu useRate: {}'.format(item[1]['user'] + item[1]['system']),
                            phone='15932972203'     # 写一个读取排班表格的函数, 获取其返回值，at当天值班的人
                        ), headers=header)
                elif item[0] == 'memory':
                    if item[1]['useRate'] > memory:
                        requests.post(url=api, data=information(
                            message='[warning] memory useRate: {:.2f}'.format(item[1]['useRate']),
                            phone='15932972203'
                        ), headers=header)
                elif item[0] == 'disk':
                    if item[1]['useRate'] > disk:
                        requests.post(url=api, data=information(
                            message='[warning] disk useRate: {}'.format(item[1]['useRate']),
                            phone='15932972203'
                        ), headers=header)



# 处理得到的日志文件，进行邮件报警
def send_mail(log_path, user, password, cpu=85, memory=50, disk=90):
    client = yagmail.SMTP(user=user, password=password, host='smtp.qq.com')

    with open(file=log_path, mode='r', encoding='utf8') as file:
        for lines in file.readlines():
            data = json.loads(lines.split('-')[-1])
            for item in data.items():
                if item[0] == 'cpu':
                    if item[1]['user'] + item[1]['system'] > cpu:
                        client.send(to=['2914283700@qq.com'],
                                    subject='system information',
                                    contents=['[waring] cpu useRate: {}'.format(item[1]['user'] + item[1]['system'])],
                                    attachments=log_path)
                elif item[0] == 'memory':
                    if item[1]['useRate'] > memory:
                        client.send(to=['2914283700@qq.com'],
                                    subject='system information',
                                    contents=['[waring] memory useRate: {:.2f}'.format(item[1]['useRate'])],
                                    attachments=log_path)
                elif item[0] == 'disk':
                    if item[1]['useRate'] > disk:
                        client.send(to=['2914283700@qq.com'],
                                    subject='system information',
                                    contents=['[waring] disk useRate: {}'.format(item[1]['useRate'])],
                                    attachments=log_path)



# 处理得到的日志文件，写入数据库
def insert_database(log_path, host, user, password, db, port=3306):
    client = pymysql.connect(host=host, port=port, user=user, password=password, db=db, charset='utf8')
    cursors = client.cursor()

    with open(file=log_path, mode='r', encoding='utf8') as file:
        for lines in file.readlines():
            times = int(lines.split()[0].strip('"'))           # 需要去掉首尾多余字符，因为
            hostname = lines.split('-')[1].strip().strip('"')  # 读出来的是字符串，带有多余的符号'"'
            data = json.loads(lines.split('-')[-1])
            for item in data.items():
                if item[0] == 'cpu':
                    sql = "insert into {} values({}, '{}', {}, {}, {});"
                    cursors.execute(sql.format(item[0], times, hostname,
                                               item[1]['user'], item[1]['system'], item[1]['idle']))
                elif item[0] == 'memory':
                    sql = "insert into {} values({}, '{}', {}, {}, {});"
                    cursors.execute(sql.format(item[0], times, hostname,
                                               item[1]['total'], item[1]['free'], item[1]['useRate']))
                elif item[0] == 'disk':
                    sql = "insert into {} values({}, '{}', {});"
                    cursors.execute(sql.format(item[0], times, hostname, item[1]['useRate']))

    client.commit()
    client.close()




# 测试
# dealLog('../getLog/monitor.log')
# dingtalk('29d923806d11a9f1836b51c8882e94cda74eded55ccd2aeac9ffa98523e14af0', '../getLog/monitor.log')
# send_mail('../getLog/monitor.log', '2914283700@qq.com', 'wxuitofvcejydebj')
# insert_database('../getLog/monitor.log', '192.168.43.102', 'Harper', '(Harper..0822)', 'systemInfo')









