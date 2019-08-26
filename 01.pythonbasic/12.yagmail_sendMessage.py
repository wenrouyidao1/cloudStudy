
import yagmail

# 建立客户端
client = yagmail.SMTP(
    user='2914283700@qq.com',           # 用户（邮箱地址）
    password='wxuitofvcejydebj',        # 授权码
    host='smtp.qq.com',                 # 固定格式（smtp.邮箱）
)

# 正文
contents = [
    'this is a message',
    'please ~ not use callback ~'
]

# 发送邮件， 添加附件
client.send(
    to=['2914283700@qq.com'],                    # 发送给谁
    subject='[python]Test message mail send ~',  # 主题
    contents=contents,                           # 正文
    attachments=['./01.iterable.py']             # 附件
)
