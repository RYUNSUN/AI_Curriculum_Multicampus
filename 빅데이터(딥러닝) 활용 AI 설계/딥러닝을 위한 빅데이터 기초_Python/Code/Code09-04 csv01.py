import csv
from tkinter.filedialog import *

with open("c:/images/csv/emp.csv") as rfp :
    reader = csv.reader(rfp) #csv 전용으로
    headerList = next(reader)
    sum = 0
    count = 0

    for cList in reader :
        sum += int(cList[3])
        count += 1
    avg = sum // count
    print(avg)
    print(cList)







