## 트리뷰(표) 활용
from tkinter import *
from tkinter import ttk # 좀 더 진보된 방법 제공
import csv
from tkinter.filedialog import  *

def openCSV() :
    global csvList
    filename = askopenfilename(parent=None,
                               filetypes=(("CSV 파일", "*.csv"), ("모든 파일", "*.*")))
    csvList = []
    with open(filename)as rfp:
        reader = csv.reader(rfp)
        headerList = next(reader)
        print(headerList)
        sum = 0
        count = 0
        for cList in reader:
            csvList.append(cList)
        print(csvList)

    # 기존 시트 클리어
    sheet.delete(*sheet.get_children()) # 시트 안에 있는 내용 삭제 / 새로운 파일을 열기 위해

    # 첫번째 열 만들기
    sheet.column('#0', width=70)  # 첫 컬럼의 내부이름
    sheet.heading('#0', text= csvList[0][0])

    # 두번째 이후 열 헤더 만들기
    sheet['columns'] = headerList[1:] # 컬럼의 제목을 csvList의 수만큼 지정
    for colName in headerList[1:] :
        sheet.column(colName,width = 70) # 내부적으로 열의 제목을 정해주는 것
        sheet.heading(colName,text=colName)

    # 내용 채우기
    for row in csvList :
        sheet.insert('','end',text = row[0],values=row[1:])

    sheet.pack(expand = 1, anchor=CENTER)

import xlrd
def openExcel() :
    global csvList
    filename = askopenfilename(parent=None,
                               filetypes=(("엑셀 파일", "*.xls;*.xlsx"), ("모든 파일", "*.*")))
    csvList = []
    workbook = xlrd.open_workbook(filename) #엑셀를 workbook으로 칭함

    print(workbook.nsheets) # workbook 안에 worksheet가 몇개 있는지 확인
    wsList = workbook.sheets()
    print(wsList[1].cell_value(0,1))
    headerList = []
    for i in range(wsList[0].ncols) :
        headerList.append(wsList[0].cell_value(0,i))

    # 내용 채우기
    for wsheet in wsList :
        rowCount = wsheet.nrows
        colCount = wsheet.ncols
        for i in range(1,rowCount) :
            tmpList=[]
            for k in range(0,colCount) :
                tmpList.append(wsheet.cell_value(i,k))
            csvList.append(tmpList)

    # for worksheet in workbook.sheets() :
    #     print(worksheet.name, worksheet.nrows, worksheet.ncols) # worksheet 이름, 행 개수, 열 개수
    #     worksheet.cell_value()

    # 기존 시트 클리어
    sheet.delete(*sheet.get_children()) # 시트 안에 있는 내용 삭제 / 새로운 파일을 열기 위해

    # 첫번째 열 만들기
    sheet.column('#0', width=70)  # 첫 컬럼의 내부이름
    sheet.heading('#0', text= csvList[0][0])

    # 두번째 이후 열 헤더 만들기
    sheet['columns'] = headerList[1:] # 컬럼의 제목을 csvList의 수만큼 지정
    for colName in headerList[1:] :
        sheet.column(colName,width = 70) # 내부적으로 열의 제목을 정해주는 것
        sheet.heading(colName,text=colName)

    # 내용 채우기
    for row in csvList :
        sheet.insert('','end',text = row[0],values=row[1:])

    sheet.pack(expand = 1, anchor=CENTER)



window = Tk()
window.geometry('400x500')
sheet = ttk.Treeview(window)

mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label='CSV 처리', menu=fileMenu)
fileMenu.add_command(label='CSV 열기', command=openCSV)
fileMenu.add_command(label='엑셀 열기', command=openExcel)
fileMenu.add_separator()



window.mainloop()