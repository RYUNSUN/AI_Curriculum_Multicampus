from sklearn import svm
from sklearn import metrics # 정답률 확인
from tkinter import *
from tkinter.simpledialog import *
from tkinter.filedialog import *
import math
import os
import os.path
from tkinter import messagebox
import time
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import joblib
import math


def changeValue(lst):
    # return [float(v) / 255 for v in lst]
    return [math.ceil(float(v)/255)for v in lst] # 소수점 올림


def studyCSV():
    global csv, train_data, train_label, test_data, test_label, clf
    global inImage, outImage,inW, inH, outW, outH, window, canvas, paper
    # 0. 훈련데이터, 테스트 데이터 준비
    filename = askopenfilename(parent=window,filetypes=(("CSV 파일", "*.csv"), ("모든파일", "*.*")))
    if filename == '' or filename == None :
        return
    csv = pd.read_csv(filename)
    train_data = csv.iloc[:, 1:].values
    train_data = list(map(changeValue, train_data))
    train_label = csv.iloc[:, 0].values
    # csv = pd.read_csv('c:/BigData/MNIST/t10k_0.5K.csv')
    # test_data = csv.iloc[:, 1:].values
    # test_data = list(map(changeValue,test_data))
    # test_label = csv.iloc[:,0].values

    # 1. Classifire 생성 (선택) --> 머신러닝 알고리즘 선택
    clf = svm.SVC(gamma='auto')
    # clf = svm.NuSVC(gamma='auto') # 70%

    # 2. 데이터로 학습 시키기
    # clf.fit( [훈련 데이터],[정답] )
    clf.fit(train_data, train_label)  # train_data:0~1 사이 값을 받음. 예전 버전에서는 train_label 문자형 안받음
    status.configure(text = '훈련 성공~~~')

def studyDump():
    global csv, train_data, train_label, test_data, test_label, clf
    global inImage, outImage,inW, inH, outW, outH, window, canvas, paper
    clf = joblib.load('mnist_model_1k.dmp')
    filename = askopenfilename(parent=window,filetypes=(("덤프 파일", "*.dmp"), ("모든파일", "*.*")))
    if filename == '' or filename == None :
        return
    clf = joblib.load(filename)
    status.configure(text='모델로딩 성공~~~')

def studySave():
    global csv, train_data, train_label, test_data, test_label, clf
    global inImage, outImage,inW, inH, outW, outH, window, canvas, paper
    saveFp = asksaveasfile(parent=window,mode='wb',defaultextension='*.raw'
                           ,filetypes=(("덤프 파일", "*.dmp"), ("모든파일", "*.*")))
    if saveFp == '' or saveFp == None :
        return
    joblib.dump(clf, saveFp)
    status.configure(text='저장 성공~~~')

def studyScore():
    global csv, train_data, train_label, test_data, test_label, clf
    global inImage, outImage,inW, inH, outW, outH, window, canvas, paper
    if clf == None :
        return
    filename = askopenfilename(parent=window,filetypes=(("CSV 파일", "*.csv"), ("모든파일", "*.*")))
    if filename == '' or filename == None :
        return
    csv = pd.read_csv(filename)
    test_data = csv.iloc[:, 1:].values
    test_data = list(map(changeValue, test_data))
    test_label = csv.iloc[:, 0].values
    results = clf.predict(test_data)
    score = metrics.accuracy_score(results,test_label)
    status.configure(text= '정답률 :' + "{0:.2f}%".format(score*100))

def predictMouse():
    global csv, train_data, train_label, test_data, test_label, clf
    global inImage, outImage,inW, inH, outW, outH, window, canvas, paper
    if clf == None : #학습되지 않으면 의미가 없으므로
        status.configure(text='모델 먼저 생성하세요.')
        return
    inImage = malloc(280,280)
    if canvas != None :
        canvas.delete()
    VIEW_Y, VIEW_X = 280, 280
    canvas = Canvas(window, height=VIEW_X, width=VIEW_Y, bg='black') # 최대 크기인 28의  보다 조금 더 크게 만들기, 검은색 배경에 흰 글씨 쓰기
    # paper = PhotoImage(height=VIEW_X, width=VIEW_Y)  # 빈 종이
    canvas.create_image((VIEW_Y // 2, VIEW_X // 2), image=paper, state='normal')
    canvas.pack(expand=1,anchor=CENTER)
    status.configure(text = '' )
    ## 마우스 이벤트
    canvas.bind("<Button-3>", rightMouseClick)
    canvas.bind("<Button-2>", midMouseClick)
    canvas.bind("<Button-1>", leftMouseClick)
    canvas.bind("<B1-Motion>", leftMouseMove)
    canvas.bind("<ButtonRelease-1>",leftMouseDrop)
    canvas.configure(cursor='mouse')

# 메모리를 할당해서 리스트(참조)를 반환하는 함수
def malloc(h,w,initValue=0) :
    retMemory = []
    for _ in range(h) :
        tmpList=[]
        for _ in range(w) :
            tmpList.append(initValue)
        retMemory.append(tmpList)
    return retMemory

def rightMouseClick(event) :
    global leftMousePressYN
    global csv, train_data, train_label, test_data, test_label, clf
    global inImage, outImage,inW, inH, outW, outH, window, canvas, paper
    ## 280 --> 28 축소
    outImage = []
    outImage = malloc(28,28)
    scale = 10
    for i in range(28) :
        for k in range(28) :
            outImage[i][k] = inImage[i*scale][k*scale]

    ## 2차원 --> 1차원
    my_data = []
    for i in range(28) :
        for k in range(28) :
            my_data.append(outImage[i][k])
    ## 출력해서 확인해보기
    for i in range(28*28) :
        print("%2d" % my_data[i], end='')
        if i%28 == 0:
            print()
    ## 예측하기
    result = clf.predict([my_data]) # 숫자 1개
    status.configure(text= '예측 숫자 ======> ' + str(result[0]))

import numpy
def midMouseClick(event) :
    global leftMousePressYN
    global csv, train_data, train_label, test_data, test_label, clf
    global inImage, outImage,inW, inH, outW, outH, window, canvas, paper

    canvas.delete('all')
    inImage = malloc(280,280)

leftMousePressYN = False
def leftMouseClick(event) :
    global leftMousePressYN
    leftMousePressYN = True

def leftMouseDrop(event) :
    global leftMousePressYN
    leftMousePressYN = False

def leftMouseMove(event) :
    global leftMousePressYN
    global csv, train_data, train_label, test_data, test_label, clf
    global inImage, outImage,inW, inH, outW, outH, window, canvas, paper
    if leftMousePressYN == False :
        return
    x = event.x ; y = event.y
    canvas.create_oval(x-15,y-15,x+15,y+15, width=0, fill='white')
    # 주위 40x40개를 찍는다.
    for i in range(-15,15,1) : # 중앙에 찍기 위한 범위 지정
        for k in range(-15,15,1) :
            if 0 <= x+i < 280 and 0 <= y+k < 280 :
                inImage[y+k][x+i] = 1


#######################
#### 전역변수 선언부 ####
#######################
inImage,outImage = [],[]
inW, inH, outW, outH = [0]*4
window, canvas, paper = None, None, None
filename = ""
panYN = False
sx,sy,ex,ey = [0] * 4
VIEW_X, VIEW_Y = 512,512 #화면에 보일 크기 (출력용)
# 머신러닝 관련 전역 변수
csv, train_data, train_label, test_data, test_label, clf = [None] * 6


#####################
#### 메인 코드부 ####
#####################
window = Tk()
window.title('머신러닝 툴 (MNIST) ver 0.01')
window.geometry("500x500")

status = Label(window, text = '',bd = 1 , relief = SUNKEN, anchor = W)
status.pack(side = BOTTOM,fill=X)

mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label='학습 시키기', menu=fileMenu)
fileMenu.add_command(label='CSV 파일로 새로 학습', command=studyCSV)
fileMenu.add_command(label='학습된 모델 가져오기', command=studyDump)
fileMenu.add_separator()
fileMenu.add_command(label='정답률 가져오기', command=studyScore)
fileMenu.add_separator()
fileMenu.add_command(label='학습 모델 저장하기', command=studySave)

predictMenu = Menu(mainMenu)
mainMenu.add_cascade(label='예측하기', menu=predictMenu)
predictMenu.add_command(label='그림 파일 불러오기', command=None) # 이전에 배웠던 방법 조합해서 사용
predictMenu.add_separator()
predictMenu.add_command(label='마우스로 직접 쓰기', command=predictMouse)


window.mainloop()