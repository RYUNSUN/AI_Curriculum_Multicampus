from tkinter import *
from tkinter import messagebox

window = Tk() # root =Tk()
mainMenu = Menu(window)
window.configure(menu=mainMenu)

def fileClick() :
    messagebox.showinfo('열기 파일','파일을 열었습니다.')

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label='파일', menu=fileMenu)
fileMenu.add_command(label='열기',command=fileClick)
fileMenu.add_separator()
fileMenu.add_command(label = "종료")

window.mainloop()