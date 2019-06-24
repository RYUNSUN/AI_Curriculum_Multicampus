from tkinter import *
from tkinter import messagebox
def clickLeft(event) :
    txt = ' '
    if event.num == 1 :
        txt += '왼쪽 버튼 : '
    elif event.num == 2 :
        txt += '가운데버튼 : '
    else :
        txt += '오른쪽 버튼 : '
    txt += str(event.x) + "," + str(event.y)
    messagebox.showinfo('요기제목',txt)

def keyPress(event) :
    messagebox.showinfo('요기제목', chr(event.keycode)) #event.keycode : 키보드 숫자

window = Tk()
window.geometry("500x300")
photo = PhotoImage(file='C:/images/Pet_GIF/Pet_GIF(128x128)/cat02_128.gif')
label1 = Label(window, image=photo)

window.bind("<Button>", clickLeft)

window.bind("<Key>", keyPress)
# window.bind("<a>", keyPress)
label1.pack(expand=1, anchor=CENTER)
window.mainloop()
