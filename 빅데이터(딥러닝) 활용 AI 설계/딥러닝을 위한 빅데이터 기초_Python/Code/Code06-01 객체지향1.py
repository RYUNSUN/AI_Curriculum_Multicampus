class Car : #클래스 생성, 클래스 이름은 대문자로 시작
    #자동차 속성
    color = None
    speed = 0 # 속성, 변수X

    #자동차의 행위(--> 함수, 기능) , 함수 대신 메서드라고 한다.
    def upSpeed(self,value):
        self.speed += value #speed는 class 속성이므로 함부로 바꾸면 안됨.
                            # 속성을 바꿔주기 위해서는 self.speed로 써줘야함.
    def downSpeed(self,value):
        self.speed -= value

########################################
myvalue = 0 # 변수
#인스턴스 생성
car1 = Car() #클래스를 활용하여 찍어냄(메모리에 저장)
car2 = Car()

car1.color = "빨강"
car1.speed = 50
car1.upSpeed(100)

print(car1.speed)

from tkinter import *
button1 = Button() # Button() : 클래스