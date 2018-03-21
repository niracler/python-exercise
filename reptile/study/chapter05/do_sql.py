import pymysql

connect = pymysql.Connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='12345678',
    db='mysql',
    charset='utf8'
)

cur = connect.cursor()
cur.execute("USE scraping")

cur.execute("SELECT * FROM pages WHERE id=2")
print(cur.fetchone())
cur.close()
connect.close()