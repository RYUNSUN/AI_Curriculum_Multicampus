## 특정 값의 모든 위치를 출력하는 프로그램
import random
myList = [random.randint(1,5) for _ in range(10)]
print(myList)
NUMBER = 5 # 찾고싶은 숫자
index = 0

# 무한 루프 돌리는게 효율적
while True :
    try:
        index = myList.index(NUMBER, index) # index : 시작점
        print(index)
        index += 1
    except :
        break


