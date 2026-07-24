import pymysql
import time

db = pymysql.connect(user='root', passwd="",host='localhost',database='yii2basic')
cur = db.cursor()
#基础执行
cur.execute("SELECT VERSION()")
data = cur.fetchone()
print(data)

#查询数据
sql = "SELECT * FROM migration"
cur.execute(sql)
result = cur.fetchall()
for i in result:
    print(i)

#插入数据
args = ("msfdsf_" + str(time.time()), time.time())
sql = "INSERT INTO migration (version, apply_time) VALUES (%s, %s)"
cur.execute(sql,args)
db.commit() #记得提交


#更新数据
sql = "UPDATE migration set version = %s WHERE apply_time = %s"
args = ("msfdsf", 1784872001)
cur.execute(sql, args)
db.commit()

#删除数据
sql = "DELETE FROM migration WHERE apply_time > %s"
args = (1784872001)
cur.execute(sql,args)
db.commit()


#事物处理
sql_1 = "DELETE FROM migration"
sql_2 = "DELTE FROM t" #不存在的SQL，执行不成功
try:
    cur.execute(sql_1)
    cur.execute(sql_2)
    db.commit()
except:
    db.rollback()
    print("事务执行错误")

db.close()