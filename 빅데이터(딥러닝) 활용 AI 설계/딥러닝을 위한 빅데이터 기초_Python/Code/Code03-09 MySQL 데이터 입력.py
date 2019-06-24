import pymysql

conn = pymysql.connect(host="192.168.56.106", user="root",password="1234",db="samsongDB", charset = "utf8") # 1. DB D연결
cur = conn.cursor() #2. 커서 생성 (트럭, 연결로프)
sql = "CREATE TABLE IF NOT EXISTS userTable2(userId INT, userName CHAR(5))"
cur.execute(sql)


sql = "INSERT INTO userTable2 VALUES(1 , '홍길동')";
cur.execute(sql)
sql= "INSERT INTO userTable2 VALUES(2 , '이순신')";
cur.execute(sql)


cur.close() # 커서 닫기
conn.commit() # 적용시키기 위해서 커밋하기
conn.close() # 6. DB 닫기 (=연결 해제)
print('OK~') # 잘 돌아가면 'OK~' 라고 출력되기