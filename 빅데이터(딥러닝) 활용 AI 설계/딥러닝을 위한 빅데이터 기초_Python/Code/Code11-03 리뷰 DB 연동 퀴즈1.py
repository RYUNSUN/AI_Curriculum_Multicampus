import pymysql

IP = '192.168.56.111'
USER = 'root'
PASS = '1234'
DB = 'quiz_DB'
CHARSET = 'utf8'

try :
    conn = pymysql.connect(host=IP, user=USER, password=PASS ,db=DB, charset = CHARSET) # 1. DB 연결
except :
    print("DB 연결 실패")
    exit() # 연결이 실패했는데 다음 줄이 진행되면 에러가 발생하므로 그냥 종료하기

cur = conn.cursor() # 트럭역할

# while True :
#     id1 = input("아이디를 입력하세요 : ")
#     if id1 == "" :
#         break
#     id2 = input("주민등록번호를 입력하세요 : ")
#     id3 = input("이메일을 입력하세요 : ")
#     sql = "INSERT INTO quiz_tbl VALUES('"+id1+"', '"+id2+"', '"+id3+"')"
#     # print(sql)
#     cur.execute(sql)

while True :
    id1, id2, id3 = input("Data Info(id/num/email) : ").split( )
    print(id1, id2, id3)
    if id1 == '' and id2 == ''and id3 == '' :
        break
    sql = "INSERT INTO quiz_tbl VALUES('"+id1+"', '"+id2+"', '"+id3+"')"
    # print(sql)
    cur.execute(sql)

conn.commit()

sql = "SELECT quiz_id, quiz_num, quiz_email FROM quiz_tbl"
cur.execute(sql)

while True :
    row = cur.fetchone()
    if row is None :
        break
    data1 = row[0]
    data2 = row[1]
    data3 = row[2]

print("아이디             주민번호             이메일")
print("--------------------------------------------")
print("%s          %s         %s" % (data1,data2,data3))
print("--------------------------------------------")

cur.close()
conn.close()
