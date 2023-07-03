import mysql.connector
myconn = mysql.connect(host="localhost" user="root",password="" database=#nameofdb)

cur = myconn.cursor()
cur.execute("select*from students")
res = cur.fetchall()

for i in res:
    print(x)

myconn.commit()
myconn.close()