import csv
from tkinter.filedialog import *
## 우리 회사 연봉 평균은?

filename = askopenfilename(parent=None, filetypes=(("csv 파일", "*.csv"), ("모든파일", "*.*")))

csvList = []
with open(filename) as rfp :
    reader = csv.reader(rfp)
    headerList = next(reader)

    sum = 0
    count = 0
    for cList in reader :
        csvList.append(cList)
    print(csvList)

## 가격을 10% 인상시키기
#1. cost 열의 위치를 찾아내기.
headerList = [data.upper().strip() for data in headerList ] #CSV 항목 대문자 변환 및 공백 제거
pos = headerList.index('COST')
for i in range(len(csvList)) :
    rowList = csvList[i]
    cost = rowList[pos]
    cost = float(cost[1:])
    cost *= 1.1
    costStr = "${0:.2f}".format(cost)
    csvList[i][pos] = costStr
print(csvList)

## 결과를 저장하기
saveFp = asksaveasfile(parent = None, mode = 'wt',
                       defaultextension = '*.csv',filetypes=(("csv 파일", "*.csv"), ("모든파일", "*.*")))

with open(saveFp.name, mode ='w',newline='') as wFp :
    writer = csv.writer(wFp)
    writer.writerow(tuple(headerList))
    for row in csvList :
        print(row)
        writer.writerow(row)




