#1. 파일 열기
inFp = open('c:/windows/win.ini','rt')
outFp = open('c:/images/new_win.ini','w')
#2. 파일 읽기 / 쓰기
## 파일 출력
while True :
    inStr = inFp.readline()
    if not inStr :
        break
    outFp.writelines(inStr)
    # print(inStr, end ='')

## 파일 입력
# inStrList = inFp.readlines()
# print(inStrList)
# for line in inStrList :
#     print(line,end='')

#3. 파일 닫기
inFp.close()
outFp.close()
print('ok~') # 잘 돌아갈때 ok라고 출력됨