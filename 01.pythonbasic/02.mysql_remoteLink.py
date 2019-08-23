
import pymysql

# 建立数据库客户端连接
client = pymysql.connect(
    host='192.168.43.102',
    port=3306,
    user='Harper',
    password='(Harper..0822)',
    db='Grade',
    charset='utf8'
)

# 建立数据库游标
cursors = client.cursor()

# 执行sql操作(将文件grade.txt中的数据写入数据库)
n = 1
with open(file='./grade_file/grade.txt', mode='r', encoding='utf8') as file:
    for lines in file:
        Name, FirstGrade, SecondGrade, Different = lines.split()
        sql = "insert into FirstStage values({}, '{}', {}, {}, {});"
        cursors.execute(sql.format(n, Name, int(FirstGrade), int(SecondGrade), int(Different)))
        n += 1

# 提交sql操作
client.commit()

# 关闭数据库连接
client.close()