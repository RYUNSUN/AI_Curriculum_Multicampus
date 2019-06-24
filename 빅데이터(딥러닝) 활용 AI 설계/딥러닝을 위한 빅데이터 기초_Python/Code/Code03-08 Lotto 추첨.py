import random

## 전역 변수 선언 ##
num = 0
lotto = []

## 메인 코드부 ##
if __name__ == '__main__':
    while True : #몇 번 돌려야 다른 숫자 6개 나올지 모르므로 무한 루프를 돌려야함.
        num = random.randint(1,45)
        if num in lotto :
            pass
        else :
            lotto.append(num) # if num not in lotto 랑 똑같은 의미
        if len(lotto) >= 6 : # 6개가 다 뽑히면 멈춰라
            break
    lotto.sort()
    print('추카추카-->', lotto)