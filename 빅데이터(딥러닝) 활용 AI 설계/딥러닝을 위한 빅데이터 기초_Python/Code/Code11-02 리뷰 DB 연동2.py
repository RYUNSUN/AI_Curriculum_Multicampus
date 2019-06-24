import pymysql

# DB 접속 정보
IP = '192.168.56.111'
USER = 'root'
PASS = '1234'
DB = 'review_db'
CHARSET = 'utf8'
conn = pymysql.connect(host=IP, user=USER, password=PASS ,db=DB, charset =CHARSET) # 1. DB 연결

cur = conn.cursor() # 트럭역할
sql = "SELECT emp_id, emp_name, emp_pay FROM emp_tbl" # * 보다는 속성을 직접 써주는 걸 권장
cur.execute(sql) # 트럭을 이용해서 내용 전달받기

#한꺼번에 담기
# rows = cur.fetchall() # 데이터베이스에서 트럭으로 내용 담기
# for row in rows :
#     print(row[0],row[1],row[2])

#한줄씩 담기
while True :
    row = cur.fetchone()
    if row is None: # 가져온게 아무것도 없을 때는 멈춰라
        break
    print(row[0],row[1],row[2])

cur.close()
conn.close()