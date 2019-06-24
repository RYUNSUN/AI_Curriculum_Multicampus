from tkinter import  *
from tkinter import messagebox
def clickButton() :
    messagebox.showinfo('요기제목','요기내용') #콜백 함수(call back function) : 바로 실행되는게 아니라 이벤트 발생 시, 실행되는 함수

window = Tk() # root =Tk()

label1 = Label(window, text = "파이썬 공부중~~") # window : text를 붙일 곳
label2 = Label(window, text = "파이썬 공부중~~", font=("궁서체",30), fg="blue")
label3 = Label(window, text = "파이썬", fg="blue", bg="red", width = 20, height = 5, anchor = SE) # anchor:배경이 위치할 곳->SE(South East)

photo = PhotoImage(file='C:/images/Pet_GIF/Pet_GIF(128x128)/cat02_128.gif')
lable4 = Label(window, image=photo)
button1 = Button(window, text = "나를 눌러줘", command=clickButton)
button2 = Button(window,image=photo, command=clickButton) # 버튼 모양을 이미지로 설정

label1.pack(side=LEFT) # lable1의 text를 실제로 붙여서 나타내는 함수
label2.pack()
label3.pack()
lable4.pack()
button1.pack()
button2.pack(side=RIGHT)# 배치 설정
window.mainloop()