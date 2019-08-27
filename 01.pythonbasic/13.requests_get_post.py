
import requests
import logging

# --------------------------------get------------------------------------------
# 网站服务状态监控(配合计划任务)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(pathname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.DEBUG,
    filename='./log_file/example.log',
    filemode='a'
)

website = (('www.baidu.com', 80), ('www.qfedu.com', 80), ('www.qq12.com', 80))

for web, port in website:
    try:
        response = requests.get(url='http://{}:{}'.format(web, port), timeout=1)
        if response.status_code in [code for code in range(200, 210)]:
            logging.debug('{} check successfully'.format(web))
        elif response.status_code in [code for code in range(400, 410)] or response.status_code in [code for code in range(500, 510)]:
            logging.error('{} check failed, status_code {}, timeout None.'.format(web, response.status_code))
    except requests.exceptions.ConnectTimeout as error:
        # 触发邮件报警或钉钉报警
        logging.error(error)
    except requests.exceptions.ConnectionError as error:
        # 触发邮件报警或钉钉报警
        logging.error(error)
    except requests.exceptions.BaseHTTPError as error:
        # 触发邮件报警或钉钉报警
        logging.error(error)
    except requests.exceptions.ReadTimeout as error:
        # 触发邮件报警或钉钉报警
        logging.error(error)

# --------------------------------post: dingtalk---------------------------------
# 钉钉报警：txt类型

import json
import requests

token = 'c8b6a3fc99a086e03bd05dffd9f979f665f300d5c2a9b458fa8f56298325281b'   # 机器人token值
api = 'https://oapi.dingtalk.com/robot/send?access_token={}'.format(token)   # api控制机器人行动

header = {'Content-Type': 'application/json'}        # 报文头部

data = {
    "msgtype": "text",
    "text": {
        "content": """
            cpu Percent: {}
            cpu User: {}
            cpu system: {}
            cpu idle: {}
        """.format(1, 2, 3, 4)       # 添加报警信息(函数的返回值)
    },
    "at": {
        "atMobiles": [
            "15222401953"            # 求得当天值班人员的电话(函数的返回值)
        ],
        "isAtAll": False
    }
}

sendData = json.dumps(data)     # 格式化为json

for bout in range(3):           # 发送三次
    requests.post(url=api, data=sendData, headers=header)

# ----------------------------------------------------------------------------------
# 钉钉报警：markdown类型

data = {
    "msgtype": "markdown",
    "markdown": {
        "title": "杭州天气",
        "text":  "#### 杭州天气 @156xxxx8827\n" +
                 "> 9度，西北风1级，空气良89，相对温度73%\n\n" +
                 "> ![screenshot](https://gw.alicdn.com/tfs/TB1ut3xxbsrBKNjSZFpXXcXhFXa-846-786.png)\n" +
                 "> ###### 10点20分发布 [天气](http://www.thinkpage.cn/) \n"
    },
    "at": {
       "atMobiles": [
           "156xxxx8827",
           "189xxxx8325"
       ],
       "isAtAll": False
    }
}

