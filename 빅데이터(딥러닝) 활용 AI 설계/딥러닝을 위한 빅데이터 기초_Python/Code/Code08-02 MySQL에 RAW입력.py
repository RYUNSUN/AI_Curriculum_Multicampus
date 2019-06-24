from tkinter import *
from tkinter.simpledialog import *
from tkinter.filedialog import *
import math
import os
import os.path
from tkinter import messagebox
import pymysql
import datetime

#####################
#### 전역 변수부 ####
#####################
# DB 접속 정보
IP_ADDR = '192.168.56.108'
USER_NAME = 'root'
USER_PASS = '1234'
DB_NAME = 'BigData_DB'
CHAR_SET = 'utf8'


################
#### 함수부 ####
################
# DB는 다른 사람들과 같이 쓰므로 계속 연동해놓기보다는 업로드나 파일 불러오면 끄는걸 권장
def selectFile() :
    filename = askopenfilename(parent=window,filetypes=(("RAW 파일", "*.raw"), ("모든파일", "*.*")))
    if filename == '' or filename == None :
        return
    edt1.insert(0, str(filename))

def uploadData() :
    # MySQL과 연결
    con = pymysql.connect(host=IP_ADDR,user=USER_NAME, password = USER_PASS, db = DB_NAME, charset = CHAR_SET)
    cur = con.cursor()

    fullname = edt1.get() #기입창의 텍스트를 문자열로 반환
    with open(fullname, 'rb') as rfp :
        binData = rfp.read()
    fname = os.path.basename(fullname) # 파일네임 추출
    fsize = os.path.getsize(fullname)
    height = width = int(math.sqrt(fsize))
    now = datetime.datetime.now()
    upDate = now.strftime('%Y-%m-%d')
    upUser = USER_NAME
    sql = "INSERT INTO rawImage_TBL(raw_id, raw_height, raw_width, raw_fname, raw_updata, raw_uploader ,raw_avg, raw_data)"
    sql += "VALUES(NULL," + str(height) + "," + str(width) + ",'" + fname + "','"
    sql += upDate + "','" + upUser + "',0 , "
    sql += " %s )"
    tupleData = (binData,)
    cur.execute(sql, tupleData) # 튜플 데이터로 저장

    con.commit() #변경할 때는 commit 해주기
    cur.close()
    con.close()

import tempfile
def downloadData() :
    # MySQL과 연결
    con = pymysql.connect(host=IP_ADDR,user=USER_NAME, password = USER_PASS, db = DB_NAME, charset = CHAR_SET)
    cur = con.cursor()
    sql = "SELECT raw_fname, raw_data FROM rawImage_TBL WHERE raw_id = 2"
    cur.execute(sql) # 튜플 데이터로 저장
    fname, binData = cur.fetchone()

    fullPath = tempfile.gettempdir() + '/' + fname
    with open(fullPath,'wb') as wfp :
        wfp.write(binData)
    print(fullPath)

    cur.close()
    con.close()
    # print(sql)

#####################
#### 메인 코드부 ####
#####################
window = Tk()
window.geometry("500x200")
window.title('Raw --> DB Ver 0.02')

edt1 = Entry(window, width = 50); # 텍스트를 입력받거나 출력하기 위한 기입창 생성
edt1.pack()
btnFile = Button(window, text = "파일선택", command=selectFile)
btnFile.pack()
btnUpload = Button(window, text = "업로드",command=uploadData)
btnUpload.pack()
btnDownload = Button(window, text = "다운로드",command=downloadData)
btnDownload.pack()

window.mainloop()