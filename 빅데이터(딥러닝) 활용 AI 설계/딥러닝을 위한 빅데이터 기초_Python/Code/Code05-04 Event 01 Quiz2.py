from tkinter import *
from tkinter import messagebox

## 전역 변수 선언부 ##
dirName = "C:/images/Pet_GIF/Pet_GIF(256x256)/"
fnameList = [ "cat01_256.gif","cat02_256.gif","cat03_256.gif",
              "cat04_256.gif","cat05_256.gif","cat06_256.gif"]

photoList = [None] * 6
num = 0 # 현재 사진 순번

## 함수 선언부 ##
def clickPrev():
    global num
    num -= 1
    if num < 0:
        num = len(fnameList)-1
    photo = PhotoImage(file=dirName + fnameList[num])
    pLabel.configure(image=photo)
    pLabel.photo = photo

def clickNext():
    global num
    num += 1
    if num >= len(fnameList) :
        num = 0
    photo = PhotoImage(file=dirName + fnameList[num])
    pLabel.configure(image=photo) #configure : 기존꺼 대신 다른거로 바꿔주는 거
    pLabel.photo=photo

def keyPress(e) :
    global  num
    # keycode number" 등으로 검색해서 키코드 번호 확인
    if e.keycode == 36 : #Home
        num = 0
    if e.keycode == 35 : #End
        num = len(fnameList)-1
    if 49 <= e.keycode <= 57 : # 1~9
        num = num + e.keycode - 48
        if num > len(fnameList)-1 :
            num = len(fnameList) - 1

    photo = PhotoImage(file=dirName + fnameList[num])
    pLabel.configure(image=photo)
    pLabel.photo=photo

## 메인 코드부 ##
window = Tk()
window.title('GIF 사진 뷰터 Beta (Ver 0.01)')
window.geometry("500x300")
window.resizable(width=FALSE, height=TRUE) # 세로 크기 변경 가능, 가로 크기 변경 X

photo = PhotoImage(file = dirName + fnameList[num])
pLabel = Label(window, image=photo)

btnPrev = Button(window, text="<< 이전 그림", command=clickPrev)
btnNext = Button(window, text="다음 그림 >>", command=clickNext)

btnPrev.place(x=150, y=10)
btnNext.place(x=250, y=10)
pLabel.place(x=15, y=50)

window.bind("<Key>", keyPress)


window.mainloop()

