import pymysql

# DB 접속 정보
IP = '192.168.56.111'
USER = 'root'
PASS = '1234'
DB = 'review_db'
PORT = '3306'
# try :
conn = pymysql.connect(host=IP, user=USER, password=PASS ,db=DB, charset ="utf8") # 1. DB 연결
# except :
#     print("DB 연결 실패")
#     exit() # 연결이 실패했는데 다음 줄이 진행되면 에러가 발생하므로 그냥 종료하기

cur = conn.cursor() # 트럭역할
sql = "INSERT INTO emp_tbl VALUES(10003, N'이순신', 5000)"

# try : # 있으면 넘어가고 없으면 생성하라는 의미
cur.execute(sql) # 트럭을 이용해서 내용 전달
# except :
#      print("입력실패~~ 확인요망..")

cur.close()
conn.commit() # 변경했을 때 커밋
conn.close()