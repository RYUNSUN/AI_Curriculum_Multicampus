from tkinter import*
from tkinter.simpledialog import *
from tkinter.filedialog import *
from tkinter import  ttk #기능이 개선됨
import os
import os.path
import math
import numpy
import pymysql
import csv
import xlrd
import xlwt
import xlsxwriter

window = Tk() # window 창 생성
# window.geometry('500x500') # window 크기
window.resizable(height=True, width=False) # 위/아래는 늘려주고, 옆으로는 확대, 축소 X

canvas = Canvas(window, width = 500, height = 700) # window 창은 캔버스의 크기에 따라 조절됨
paper = canvas.create_image(width=500,height=500)
# canvas.create_line(10,10,100,100, width=5, fill ='red') # line(x1,y1,x2,y2)
paper = PhotoImage(width=500,height=500)  # 빈 종이
canvas.create_image((500 // 2, 500 // 2), image=paper, state='normal')  # state는 보통 normal 씀 , 500//2 => 중앙 의미
# 한칸씩 넣으면 느리니깐 문자로 한줄씩 만들어 출력하기



canvas.pack(expand=1, anchor=CENTER) # 캔버스가 중앙에 위치
window.mainloop()
