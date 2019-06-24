import pymysql

conn = pymysql.connect(host="192.168.56.103", user="root", password="1234", db="mission03", charset="utf8")
cur = conn.cursor()
sql = "CREATE TABLE IF NOT EXISTS missionTable(userID INT(5), userName CHAR(5), employYear INT(5))"
cur.execute(sql)

while True :
    data1 = input("사번 -->")
    if data1 == '0':
        break;
    data2 = input("이름 -->")
    data3 = input("입사연도 -->")
    data = "INSERT INTO missionTable VALUES("+ data1 +",'"+ data2 +"',"+data3+")"
    cur.execute(data)

conn.commit()

sql = "SELECT * FROM missionTable" #sql에 명령
cur.execute(sql)

print("  사번      이름     입사연도")
print(" -----------------------------")

while True :
    row = cur.fetchone()

    if row == None:
        break
    data1 = row[0]
    data2 = row[1]
    data3 = row[2]
    print("%5d     %5s     %5d" % (data1, data2, data3))

print(" -----------------------------")
conn.close()
