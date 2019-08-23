
# 从数据库读取数据生成报表
import pymysql
import openpyxl

client = pymysql.connect(
    host='192.168.43.102',
    port=3306,
    user='Harper',
    password='(Harper..0822)',
    db='webInfo',
    charset='utf8'
)
cursors = client.cursor()

sql = "select * from {};"
cursors.execute(sql.format('ips'))
result = cursors.fetchall()
# print(result)

file = openpyxl.Workbook()
sheet = file['Sheet']
for lines in result:
    sheet.append(lines)
file.save('./excel_file/webInfo.xlsx')

client.close()
