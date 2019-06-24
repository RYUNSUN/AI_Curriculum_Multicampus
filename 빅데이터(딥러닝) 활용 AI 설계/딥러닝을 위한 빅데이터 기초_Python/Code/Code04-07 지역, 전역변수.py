def func1() :
    global a # a를 전역변수로 지정, 값을 셋팅할 때는 global을 써줘야함
    a = 10 # 지역변수
    print('func1() --> ', a)

def func2() :
    global a # 주요한 함수 안에는 global 값으로 지정해줘야함. 지역과 전역은 반드시 이름을 다르게 해야함
    print('func2() --> ', a)

# 변수 선언부
a = 1234

## 메인 코드부
func1()
print(a) # a가 10으로 변경되어 있기를 기대함
func2()
