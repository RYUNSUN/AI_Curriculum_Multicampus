import pymysql

conn = pymysql.connect(host="192.168.56.106", user="root",password="1234",db="samsongDB", charset = "utf8") # 1. DB D연결
cur = conn.cursor() #2. 커서 생성 (트럭, 연결로프)
sql = "SELECT * FROM userTable2" #sql에 명령
cur.execute(sql)

rows = cur.fetchall() #select 한 데이터 모두 가져오기

print(rows)

cur.close() # 커서 닫기
conn.close() # 6. DB 닫기 (=연결 해제)
print('OK~') # 잘 돌아가면 'OK~' 라고 출력되기