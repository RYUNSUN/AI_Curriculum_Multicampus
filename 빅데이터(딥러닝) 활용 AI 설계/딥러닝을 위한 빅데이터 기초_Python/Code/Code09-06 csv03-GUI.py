## 트리뷰(표) 활용
from tkinter import *
from tkinter import ttk # 좀 더 진보된 방법 제공

window = Tk()
window.geometry('800x500')
sheet = ttk.Treeview(window)
# 첫번째 열 만들기
sheet.column('#0', width = 70) # 첫 컬럼의 내부이름
sheet.heading('#0', text = '제목1')

# 두번째 이후 열 헤더 만들기
sheet['columns'] =("A","B","C") # 두번째 이후 컬럼의 내부이름 (내맘대로)
sheet.column("A",width = 70); sheet.heading('A',text='제목2')
sheet.column("B",width = 70); sheet.heading('B',text='제목3')
sheet.column("C",width = 70); sheet.heading('C',text='제목4')

#내용 채우기
sheet.insert('', 'end',text='1열 값1', values = ('2열 값1','3열 값1','4열 값1'))
sheet.insert('', 'end',text='1열 값2', values = ('2열 값2','3열 값2','4열 값2'))
sheet.insert('', 'end',text='1열 값3', values = ('2열 값3','3열 값3','4열 값3'))

sheet.pack()
window.mainloop()