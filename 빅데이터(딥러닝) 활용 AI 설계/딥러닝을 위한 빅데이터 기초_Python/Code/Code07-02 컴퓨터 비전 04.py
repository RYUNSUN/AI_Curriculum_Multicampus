from tkinter import *
from tkinter.simpledialog import *
from tkinter.filedialog import *
import math
import os
import os.path
from tkinter import messagebox



#####################
#### 함수 선언부 ####
#####################
# 메모리를 할당해서 리스트(참조)를 반환하는 함수
def melloc(h,w,initValue=0) :
    retMemory = []
    for _ in range(h) :
        tmpList=[]
        for _ in range(w) :
            tmpList.append(initValue)
        retMemory.append(tmpList)
    return retMemory

# 파일을 메모리로 로딩하는 함수
def loadImage(fname) :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    fsize = os.path.getsize(fname) # 파일의 크기(바이트)
    inH =inW = int(math.sqrt(fsize)) # 핵심 코드 (메모리를 확보하기 위한 파일의 크기 확인)

    ## 입력영상 메모리 확보 ##
    inImage= [] # 이미지가 누적되지 않고 새롭게 불러올 수 있도록 초기화
    inImage = melloc(inH, inW)

    # 파일 --> 메모리
    with open(filename,'rb') as rFp :
        for i in range(inH) :
            for k in range(inW) :
                inImage[i][k] = int(ord(rFp.read(1))) #1바이트씩 읽힘
    # print(inH,inW)
    # print(int(ord(inImage[100][100])))


# 파일을 선택해서 메모리로 로딩하는 함수
# p.353
def openImage() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    filename = askopenfilename(parent=window,filetypes=(("RAW 파일", "*.raw"), ("모든파일", "*.*")))
    if filename == '' or filename == None :
        return
    loadImage(filename)
    eqaulImage()

import struct
def saveImage() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    saveFp = asksaveasfile(parent=window,mode='wb',defaultextension='*.raw'
                           ,filetypes=(("RAW 파일", "*.raw"), ("모든파일", "*.*")))
    if saveFp == '' or saveFp == None :
        return
    for i in range(outH) :
        for k in range(outW) :
            saveFp.wirte(struct.pack('B',outImage[i][k])) #struct는 1바이트씩 저장을 도와주는 함수
    saveFp.close()

def displayImage() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    if canvas!= None : # 예전에 실행한 적이 있다.
        canvas.destroy() # 캔버스를 뜯어내는 것
    ## 화면 크기를 조절
    window.geometry(str(outH) + 'x' + str(outW)) # 벽
    canvas = Canvas(window, height = outH, width = outW) # 보드
    paper = PhotoImage(height = outH, width = outW) # 빈 종이
    canvas.create_image((outH//2, outW//2), image=paper, state='normal') # state는 보통 normal 씀
    # ## 출력영상 ---> 화면에 한점씩 찍자
    # for i in range(outH) :
    #     for k in range(outW) :
    #         r = g = b = outImage[i][k]
    #         paper.put("#%02x%02x%02x" % (r, g, b),(k, i)) # RRGGBB 16진수로 표현한 것, x는 16진수
    ## 성능 개선
    rgbStr = '' #전체 픽셀의 문자열을 저장
    for i in range(outH) :
        tmpStr = ''
        for k in range(outW) :
            r = g = b = outImage[i][k]
            tmpStr += ' #%02x%02x%02x' % (r,g,b) # 문자열은 한칸씩 띄기
        rgbStr += '{' + tmpStr + '} ' # 마지막 중괄호 뒤에 한칸 띄기
    paper.put(rgbStr)

    ## 마우스 이벤트
    canvas.bind("<Button-1>", mouseClick)
    canvas.bind("<ButtonRelease-1>",mouseDrop)
    canvas.pack(expand=1,anchor=CENTER)


#################################################
####컴퓨터 비전(영상처리) 알고리즘 함수 모음 ####
#################################################

# 동일영상 알고리즘
def eqaulImage() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    ## 중요! 코드, 출력영상 크기 결정##
    outH = inH
    outW = inW
    ###### 메모리 할당 ###########################
    outImage = []
    outImage = melloc(outH, outW)
    ###### 진짜 컴퓨터 비전 알고리즘 #####
    for i in range(inH) :
        for k in range(inW) :
            outImage[i][k] = inImage[i][k]
    ## 출력
    displayImage()

# 화소점 처리 알고리즘(밝게하기)
def addImage() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    ## 중요! 코드, 출력영상 크기 결정##
    outH = inH
    outW = inW
    ###### 메모리 할당 ###########################
    outImage = []
    outImage = melloc(outH, outW)
    ###### 진짜 컴퓨터 비전 알고리즘 #####
    value = askinteger("밝게하기","밝게할 값 -->",minvalue=1,maxvalue=255)
    for i in range(inH) :
        for k in range(inW) :
            outImage[i][k] = inImage[i][k] + value
            if outImage[i][k] > 255 :
                outImage[i][k] = 255

    ## 출력
    displayImage()

# 화소점 처리 알고리즘(어둡게하기)
def minusImage() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    ## 중요! 코드, 출력영상 크기 결정##
    outH = inH
    outW = inW
    ###### 메모리 할당 ###########################
    outImage = []
    outImage = melloc(outH, outW)
    ###### 진짜 컴퓨터 비전 알고리즘 #####
    value = askinteger("어둡게하기","어둡게할 값 -->",minvalue=1,maxvalue=255)
    for i in range(inH) :
        for k in range(inW) :
            outImage[i][k] = inImage[i][k] - value
            if outImage[i][k] < 1 :
                outImage[i][k] = 1

    ## 출력
    displayImage()

# 화소점 처리 알고리즘(영상 곱셈)
def multiplyImage() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    ## 중요! 코드, 출력영상 크기 결정##
    outH = inH
    outW = inW
    ###### 메모리 할당 ###########################
    outImage = []
    outImage = melloc(outH, outW)
    ###### 진짜 컴퓨터 비전 알고리즘 #####
    value = askinteger("영상 곱셈","곱할 값 -->",minvalue=1,maxvalue=255)
    for i in range(inH) :
        for k in range(inW) :
            outImage[i][k] = inImage[i][k] * value
            if outImage[i][k] > 255 :
                outImage[i][k] = 255

    ## 출력
    displayImage()

# 화소점 처리 알고리즘(영상 나눗셈)
def divisionImage() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    ## 중요! 코드, 출력영상 크기 결정##
    outH = inH
    outW = inW
    ###### 메모리 할당 ###########################
    outImage = []
    outImage = melloc(outH, outW)
    ###### 진짜 컴퓨터 비전 알고리즘 #####
    value = askinteger("영상 나눗셈","나눌 값 -->",minvalue=1,maxvalue=255)
    for i in range(inH) :
        for k in range(inW) :
            outImage[i][k] = inImage[i][k] // value
            if outImage[i][k] < 1 :
                outImage[i][k] = 1

    ## 출력
    displayImage()

# 화소점 처리 알고리즘(화소값 반전)
def reversedImage() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    ## 중요! 코드, 출력영상 크기 결정##
    outH = inH
    outW = inW
    ###### 메모리 할당 ###########################
    outImage = []
    outImage = melloc(outH, outW)
    ###### 진짜 컴퓨터 비전 알고리즘 #####
    for i in range(inH) :
        for k in range(inW) :
            outImage[i][k] = 255 - inImage[i][k]

    ## 출력
    displayImage()

# 화소점 처리 알고리즘(이진화)
def binaryImage() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    ## 중요! 코드, 출력영상 크기 결정##
    outH = inH
    outW = inW
    ###### 메모리 할당 ###########################
    outImage = []
    outImage = melloc(outH, outW)
    ###### 진짜 컴퓨터 비전 알고리즘 #####
    ##영상의 평균 구하기
    sum = 0
    for i in range(inH) :
        for k in range(inW) :
            sum += inImage[i][k]
    avg = sum // (inW * inH)

    for i in range(inH) :
        for k in range(inW) :
            if inImage[i][k] > avg :
                outImage[i][k] = 255
            else :
                outImage[i][k] = 0

    ## 출력
    displayImage()

# 화소점 처리 알고리즘(입출력 영상의 평균값 구하기)
def averageImage() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    ## 중요! 코드, 출력영상 크기 결정##
    outH = inH
    outW = inW
    ###### 메모리 할당 ###########################
    outImage = []
    outImage = melloc(outH, outW)
    ###### 진짜 컴퓨터 비전 알고리즘 #####
    hap = 0
    for i in range(inH) :
        for k in range(inW) :
            outImage[i][k] = inImage[i][k]
            hap += outImage[i][k]
        average = hap / (outH * outW)
    print(average)

    ## 출력
    messagebox.showinfo('입출력 영상 평균값', '%7.4f' % average)

# 화소점 처리 알고리즘(감마보정)
# 감마값이 1보다 크면 영상이 어두워지고, 1보다 작으면 영상이 밝아짐
def gammaImage() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    ## 중요! 코드, 출력영상 크기 결정##
    outH = inH
    outW = inW
    ###### 메모리 할당 ###########################
    outImage = []
    outImage = melloc(outH, outW)
    ###### 진짜 컴퓨터 비전 알고리즘 #####
    value = askfloat("감마 보정","감마 값 -->",minvalue=0,maxvalue=255)
    for i in range(inH) :
        for k in range(inW) :
            outImage[i][k] = inImage[i][k]//(1/value)
            if outImage[i][k] < 0 :
                outImage[i][k] = 0

    ## 출력
    displayImage()

# 파라볼라 알고리즘 with LUT
# Out = 255 - 255*(Input/128-1)^2
# 입체 형태로 출력
def paraImage() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    ## 중요! 코드, 출력영상 크기 결정##
    outH = inH
    outW = inW
    ###### 메모리 할당 ###########################
    outImage = []
    outImage = melloc(outH, outW)
    ###### 진짜 컴퓨터 비전 알고리즘 #####
    LUT = [0 for _ in range(256)]
    for input in range(256) :
        LUT[input] = int(255 - 255 * math.pow(input / 128 - 1, 2))

    for i in range(inH) :
        for k in range(inW) :
            input = inImage[i][k]
            outImage[i][k] = LUT[inImage[i][k]]
    ## 출력
    displayImage()


# 상하반전 알고리즘
def upDownImage() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    ## 중요! 코드, 출력영상 크기 결정##
    outH = inH
    outW = inW
    ###### 메모리 할당 ###########################
    outImage = []
    outImage = melloc(outH, outW)
    ###### 진짜 컴퓨터 비전 알고리즘 #####
    for i in range(inH) :
        for k in range(inW) :
            outImage[inH-i-1][k] = inImage[i][k]
    ## 출력
    displayImage()

# 오른쪽 90도 회전 알고리즘
def rotationImage() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    ## 중요! 코드, 출력영상 크기 결정##
    outH = inH
    outW = inW
    ###### 메모리 할당 ###########################
    outImage = []
    outImage = melloc(outH, outW)
    ###### 진짜 컴퓨터 비전 알고리즘 #####
    for i in range(inH) :
        for k in range(inW) :
            outImage[k][inW-i-1] = inImage[i][k]
    ## 출력
    displayImage()


# 상하 이동 알고리즘
def updownMoveImage() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    ## 중요! 코드, 출력영상 크기 결정##
    outH = inH
    outW = inW
    ###### 메모리 할당 ###########################
    outImage = []
    outImage = melloc(outH, outW)
    ###### 진짜 컴퓨터 비전 알고리즘 #####
    value = askinteger("이동 값을 입력하세요.","이동할 값 -->")

    # 위로 이동
    for i in range(inH) :
        for k in range(inW) :
            if i - value > 0 :
                outImage[i-value][k] = inImage[i][k]
            # else :
            #     outImage[i][k] = 0

    ## 출력
    displayImage()

## 마우스 화면이동 알고리즘
def moveImage() :
    global panYN
    panYN = True
    canvas.configure(cursor = 'mouse')

def mouseClick(event) :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH,sx,sy,ex,ey,panYN
    if panYN == False :
        return
    sx = event.x
    sy = event.y

def mouseDrop(event) :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH,sx,sy,ex,ey,panYN
    if panYN == False :
        return
    ex = event.x
    ey = event.y
    ## 중요! 코드, 출력영상 크기 결정##
    outH = inH
    outW = inW
    ###### 메모리 할당 ###########################
    outImage = []
    outImage = melloc(outH, outW)
    ###### 진짜 컴퓨터 비전 알고리즘 #####
    mx = sx - ex
    my = sy - ey
    for i in range(inH) :
        for k in range(inW) :
            if 0 <= i-my < outW and 0 <= k-mx < outH :
                outImage[i-my][k-mx] = inImage[i][k]
    panYN = False
    ## 출력
    displayImage()

# 영상 축소 알고리즘
def zoomOutImage() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    scale = askinteger("축소","값 -->",minvalue=2,maxvalue=16)
    ## 중요! 코드, 출력영상 크기 결정##
    outH = inH//scale
    outW = inW//scale
    ###### 메모리 할당 ###########################
    outImage = []
    outImage = melloc(outH, outW)
    ###### 진짜 컴퓨터 비전 알고리즘 #####
    ##대표값을 가져와서 축소하므로 영상이 아닌 경우 모양이 이상할 수 있음.
    ## 이때는 축소할 값들의 평균값 또는 중위수를 이용해서 축소. 성능이 떨어질 수 있음
    # 전방향
    # for i in range(inH) :
    #     for k in range(inW) :
    #         outImage[i//scale][k//scale] = inImage[i][k]
    ## 성능개선 (역방향)
    for i in range(outH) :
        for k in range(outW) :
            outImage[i][k] = inImage[i*scale][k*scale]
    ## 출력
    displayImage()

# 영상 축소 알고리즘 (평균변환)
def zoomOutImage2() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    scale = askinteger("축소","값 -->",minvalue=2,maxvalue=16)
    ## 중요! 코드, 출력영상 크기 결정##
    outH = inH//scale
    outW = inW//scale
    ###### 메모리 할당 ###########################
    outImage = []
    outImage = melloc(outH, outW)
    ###### 진짜 컴퓨터 비전 알고리즘 #####
    for i in range(inH) :
        for k in range(inW) :
            outImage[i // scale][k // scale] += inImage[i][k]
    for i in range(outH) :
        for k in range(outW) :
            outImage[i][k] //= (scale * scale)
    ## 출력
    displayImage()


# 영상 확대 알고리즘
def zoomInImage() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    scale = askinteger("확대","값 -->",minvalue=2,maxvalue=4)
    ## 중요! 코드, 출력영상 크기 결정##
    outH = inH*scale
    outW = inW*scale
    ###### 메모리 할당 ###########################
    outImage = []
    outImage = melloc(outH, outW)
    ###### 진짜 컴퓨터 비전 알고리즘 #####
    #전방향
    # for i in range(inH) :
    #     for k in range(inW) :
    #         outImage[i*scale][k*scale] = inImage[i][k]

    #역방향
    for i in range(outH) :
        for k in range(outW) :
            outImage[i][k] = inImage[i//scale][k//scale]

    ## 출력
    displayImage()

# 영상 확대 알고리즘(양선형 보간)
# 깨끗하게 확대되기 때문에 추후에 딥러닝하면 좋은 결과가 나올 수 있음
def zoomInImage2() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    scale = askinteger("확대","값 -->",minvalue=2,maxvalue=4)
    ## 중요! 코드, 출력영상 크기 결정##
    outH = inH*scale
    outW = inW*scale
    ###### 메모리 할당 ###########################
    outImage = []
    outImage = melloc(outH, outW)
    ###### 진짜 컴퓨터 비전 알고리즘 #####
    rH,rW,iH, iW = [0]*4 # 실수 위치 및 정수 위치
    x,y = 0,0 # 실수와 정수의 차이값
    C1,C2,C3,C4 = [0] * 4 # 결정할 위치(N)의 상하좌우 픽셀
    for i in range(outH) :
        for k in range(outW) :
            rH = i / scale
            rW = k / scale
            iH = int(rH)
            iW = int(rW)
            x = rW - iW
            y = rH - iH
            if 0 <= iH < inH-1 and 0 <= iW < inW-1 :
                C1 = inImage[iH][iW]
                C2 = inImage[iH][iW+1]
                C3 = inImage[iH+1][iW+1]
                C4 = inImage[iH+1][iW]
                newValue = C1 * (1-y) * (1-x) + C2 * (1-y) * x + C3*y*x + C4 * y * (1-x)
                outImage[i][k] = int(newValue)
    ## 출력
    displayImage()


# 영상 회전 알고리즘
def rotateImage() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    angle = askinteger("회전","값 -->",minvalue=1,maxvalue=360)
    ## 중요! 코드, 출력영상 크기 결정##
    outH = inH
    outW = inW
    ###### 메모리 할당 ###########################
    outImage = []
    outImage = melloc(outH, outW)
    ###### 진짜 컴퓨터 비전 알고리즘 #####
    radian = angle * math.pi / 180 # radian degree 수식
    for i in range(inH) :
        for k in range(inW) :
            xs = i
            ys = k
            xd = int(math.cos(radian) * xs - math.sin(radian) * ys)
            yd = int(math.sin(radian) * xs + math.cos(radian) * ys)
            if 0<= xd < inH and 0 <= yd < inW :
                outImage[xd][yd] = inImage[i][k]

    ## 출력
    displayImage()

# 히스토그램
import matplotlib.pyplot as plt
def histoImage() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    inCountList = [0] * 256
    outCountList =[0]*256
    # countList = [0] * 256

    # for i in range(outH) :
    #     for k in range(outW) :
    #         CountList[inImage[i][k]] += 1

    for i in range(inH) :
        for k in range(inW) :
            inCountList[inImage[i][k]] += 1

    for i in range(outH) :
        for k in range(outW) :
            outCountList[outImage[i][k]] += 1

    plt.plot(inCountList)
    plt.plot(outCountList)
    # plt.plot(countList)
    plt.show()

# 스트레칭 알고리즘
def stretchImage() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    ## 중요! 코드, 출력영상 크기 결정##
    outH = inH
    outW = inW
    ###### 메모리 할당 ###########################
    outImage = []
    outImage = melloc(outH, outW)
    ###### 진짜 컴퓨터 비전 알고리즘 #####
    maxVal = minVal = inImage[0][0]

    for i in range(inH) :
        for k in range(inW) :
            if inImage[i][k] < minVal :
                minVal = inImage[i][k]
            elif inImage[i][k] > maxVal :
                maxVal = inImage[i][k]

    for i in range(inH) :
        for k in range(inW) :
            outImage[i][k] = int(((inImage[i][k] - minVal) / (maxVal - minVal)) * 255)

    ## 출력
    displayImage()

# End-In 탐색 알고리즘
def endinImage() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    ## 중요! 코드, 출력영상 크기 결정##
    outH = inH
    outW = inW
    ###### 메모리 할당 ###########################
    outImage = []
    outImage = melloc(outH, outW)
    ###### 진짜 컴퓨터 비전 알고리즘 #####
    maxVal = minVal = inImage[0][0]

    for i in range(inH) :
        for k in range(inW) :
            if inImage[i][k] < minVal :
                minVal = inImage[i][k]
            elif inImage[i][k] > maxVal :
                maxVal = inImage[i][k]

    minAdd = askinteger("최소","최소추가 -->",minvalue=0,maxvalue=255)
    maxAdd = askinteger("최대","최대감소 -->",minvalue=0,maxvalue=255)

    minVal += minAdd
    maxVal -= maxAdd

    for i in range(inH) :
        for k in range(inW) :
            value = int(((inImage[i][k] - minVal) / (maxVal - minVal)) * 255)
            if value < 0 :
                value = 0
            elif value > 255 :
                value = 255
            outImage[i][k] = value
    ## 출력
    displayImage()

# 히스토그램 평활화
import matplotlib.pyplot as plt
def histoEqualImage() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    histo = [0] * 256
    sumHisto = [0] * 256
    normalHisto = [0]*256
    sum = 0

    ## 중요! 코드, 출력영상 크기 결정##
    outH = inH
    outW = inW
    ###### 메모리 할당 ###########################
    outImage = []
    outImage = melloc(outH, outW)

    for i in range(inH) :
        for k in range(inW) :
            histo[inImage[i][k]] += 1

    #누적 히스토그램
    sValue = 0
    for i in range(len(histo)) :
        sValue += histo[i]
        sumHisto[i] =sValue

    #정규화 누적 히스토그램
    for i in range(len(sumHisto)) :
        normalHisto[i] = int(sumHisto[i] / (inW*inH)*255)

    # 영상처리
    for i in range(inH) :
        for k in range(inW) :
            outImage[i][k] = normalHisto[inImage[i][k]]

    displayImage()

    plt.plot(histo)
    plt.show()

# 엠보싱 처리
def embossImage() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    ## 중요! 코드, 출력영상 크기 결정##
    outH = inH
    outW = inW
    ###### 메모리 할당 ###########################
    outImage = []
    outImage = melloc(outH, outW)
    ###### 진짜 컴퓨터 비전 알고리즘 #####
    MSIZE = 3
    mask = [ [-1, 0, 0],
             [ 0, 0, 0],
             [ 0, 0, 1] ]
    ## 임시 입력영상 메모리 확보
    tmpInImage = melloc(inH + MSIZE -1, inW + MSIZE -1, 127)  #127 중간값
    tmpOutImage = melloc(outH, outW)
    ## 원 입력 ---> 임시 입력
    for i in range(inH) :
        for k in range(inW) :
            tmpInImage[i+MSIZE//2][k+MSIZE//2] = inImage[i][k]
    ## 회선연산 : (1,1)이 중심
    for i in range(MSIZE//2,inH+MSIZE//2) :
        for k in range(MSIZE//2,inW+MSIZE//2) :
            # 각 점을 처리
            s = 0.0
            for m in range(0 ,MSIZE) :
                for n in range(0,MSIZE) :
                    s += mask[m][n]*tmpInImage[i+m-MSIZE//2][k+n-MSIZE//2] # 마스크와 영상과 자리 맞추기
            tmpOutImage[i-MSIZE//2][k-MSIZE//2] = s

    ## 127 더하기 (선택)
    for i in range(outH) :
        for k in range(outW) :
            tmpOutImage[i][k] += 127

    ## 임시 출력 --> 원 출력
    for i in range(outH) :
        for k in range(outW) :
            value = tmpOutImage[i][k]
            if value > 255 :
                value = 255
            elif value < 0 :
                value = 0
            outImage[i][k] = int(value)


    ## 출력
    displayImage()

# 영상 회전 알고리즘
def rotateImage2() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    angle = askinteger("회전","값 -->",minvalue=1,maxvalue=360)
    ## 중요! 코드, 출력영상 크기 결정##
    outH = inH
    outW = inW
    ###### 메모리 할당 ###########################
    outImage = []
    outImage = melloc(outH, outW)
    ###### 진짜 컴퓨터 비전 알고리즘 #####
    radian = angle * math.pi / 180 # radian degree 수식
    h = inH - 1
    cx = inW/2
    cy = inH/2
    for i in range(inH) :
        for k in range(inW) :
            xs = i
            ys = k
            xd = int((xs - cx) * math.cos(radian) - (ys - cy) * math.sin(radian) + cx)
            yd = int((xs - cx) * math.sin(radian) + (ys - cy) * math.cos(radian) + cy)
            if 0<= xd < inH and 0 <= yd < inW :
                outImage[xd][yd] = inImage[i][k]

    ## 출력
    displayImage()

# 블러링 처리
def blurImage() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    ## 중요! 코드, 출력영상 크기 결정##
    outH = inH
    outW = inW
    ###### 메모리 할당 ###########################
    outImage = []
    outImage = melloc(outH, outW)
    ###### 진짜 컴퓨터 비전 알고리즘 #####
    # MSIZE = 3
    # mask = [ [1/9, 1/9, 1/9],
    #          [1/9, 1/9, 1/9],
    #          [1/9, 1/9, 1/9] ]

    MSIZE = 5
    mask = [ [1/25, 1/25, 1/25, 1/25, 1/25],
             [1/25, 1/25, 1/25, 1/25, 1/25],
             [1/25, 1/25, 1/25, 1/25, 1/25],
             [1/25, 1/25, 1/25, 1/25, 1/25],
             [1/25, 1/25, 1/25, 1/25, 1/25]]

    ## 임시 입력영상 메모리 확보
    tmpInImage = melloc(inH + MSIZE -1, inW + MSIZE -1, 127)  #127 중간값
    tmpOutImage = melloc(outH, outW)
    ## 원 입력 ---> 임시 입력
    for i in range(inH) :
        for k in range(inW) :
            tmpInImage[i+MSIZE//2][k+MSIZE//2] = inImage[i][k]
    ## 회선연산 : (1,1)이 중심
    for i in range(MSIZE//2,inH+MSIZE//2) :
        for k in range(MSIZE//2,inW+MSIZE//2) :
            # 각 점을 처리
            s = 0.0
            for m in range(0 ,MSIZE) :
                for n in range(0,MSIZE) :
                    s += mask[m][n]*tmpInImage[i+m-MSIZE//2][k+n-MSIZE//2] # 마스크와 영상과 자리 맞추기
            tmpOutImage[i-MSIZE//2][k-MSIZE//2] = s

    ## 임시 출력 --> 원 출력
    for i in range(outH) :
        for k in range(outW) :
            value = tmpOutImage[i][k]
            if value > 255 :
                value = 255
            elif value < 0 :
                value = 0
            outImage[i][k] = int(value)

    ## 출력
    displayImage()

# 샤프닝 처리
def sharpImage() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    ## 중요! 코드, 출력영상 크기 결정##
    outH = inH
    outW = inW
    ###### 메모리 할당 ###########################
    outImage = []
    outImage = melloc(outH, outW)
    ###### 진짜 컴퓨터 비전 알고리즘 #####
    MSIZE = 3
    # mask = [ [0, -1,  0],
    #          [-1, 5, -1],
    #          [0, -1,  0] ]

    mask = [ [-1, -1,  -1],
             [-1, 9, -1],
             [-1, -1,  -1] ]

    ## 임시 입력영상 메모리 확보
    tmpInImage = melloc(inH + MSIZE -1, inW + MSIZE -1, 127)  #127 중간값
    tmpOutImage = melloc(outH, outW)
    ## 원 입력 ---> 임시 입력
    for i in range(inH) :
        for k in range(inW) :
            tmpInImage[i+MSIZE//2][k+MSIZE//2] = inImage[i][k]
    ## 회선연산 : (1,1)이 중심
    for i in range(MSIZE//2,inH+MSIZE//2) :
        for k in range(MSIZE//2,inW+MSIZE//2) :
            # 각 점을 처리
            s = 0.0
            for m in range(0 ,MSIZE) :
                for n in range(0,MSIZE) :
                    s += mask[m][n]*tmpInImage[i+m-MSIZE//2][k+n-MSIZE//2] # 마스크와 영상과 자리 맞추기
            tmpOutImage[i-MSIZE//2][k-MSIZE//2] = s

    ## 임시 출력 --> 원 출력
    for i in range(outH) :
        for k in range(outW) :
            value = tmpOutImage[i][k]
            if value > 255 :
                value = 255
            elif value < 0 :
                value = 0
            outImage[i][k] = int(value)

    ## 출력
    displayImage()

# 가우시안 필터링 처리
def gaussianImage() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    ## 중요! 코드, 출력영상 크기 결정##
    outH = inH
    outW = inW
    ###### 메모리 할당 ###########################
    outImage = []
    outImage = melloc(outH, outW)
    ###### 진짜 컴퓨터 비전 알고리즘 #####
    MSIZE = 3
    mask = [ [1/16, 1/8, 1/16],
             [1/8, 1/4, 1/8],
             [1/16, 1/8, 1/16] ]

    ## 임시 입력영상 메모리 확보
    tmpInImage = melloc(inH + MSIZE -1, inW + MSIZE -1, 127)  #127 중간값
    tmpOutImage = melloc(outH, outW)
    ## 원 입력 ---> 임시 입력
    for i in range(inH) :
        for k in range(inW) :
            tmpInImage[i+MSIZE//2][k+MSIZE//2] = inImage[i][k]
    ## 회선연산 : (1,1)이 중심
    for i in range(MSIZE//2,inH+MSIZE//2) :
        for k in range(MSIZE//2,inW+MSIZE//2) :
            # 각 점을 처리
            s = 0.0
            for m in range(0 ,MSIZE) :
                for n in range(0,MSIZE) :
                    s += mask[m][n]*tmpInImage[i+m-MSIZE//2][k+n-MSIZE//2] # 마스크와 영상과 자리 맞추기
            tmpOutImage[i-MSIZE//2][k-MSIZE//2] = s

    ## 임시 출력 --> 원 출력
    for i in range(outH) :
        for k in range(outW) :
            value = tmpOutImage[i][k]
            if value > 255 :
                value = 255
            elif value < 0 :
                value = 0
            outImage[i][k] = int(value)

    ## 출력
    displayImage()

# 고주파
def highFrequencyImage() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    ## 중요! 코드, 출력영상 크기 결정##
    outH = inH
    outW = inW
    ###### 메모리 할당 ###########################
    outImage = []
    outImage = melloc(outH, outW)
    ###### 진짜 컴퓨터 비전 알고리즘 #####
    MSIZE = 3
    mask = [ [-1/9, -1/9, -1/9],
             [-1/9, 8/9, -1/9],
             [-1/9, -1/9, -1/9] ]

    ## 임시 입력영상 메모리 확보
    tmpInImage = melloc(inH + MSIZE -1, inW + MSIZE -1, 127)  #127 중간값
    tmpOutImage = melloc(outH, outW)
    ## 원 입력 ---> 임시 입력
    for i in range(inH) :
        for k in range(inW) :
            tmpInImage[i+MSIZE//2][k+MSIZE//2] = inImage[i][k]
    ## 회선연산 : (1,1)이 중심
    for i in range(MSIZE//2,inH+MSIZE//2) :
        for k in range(MSIZE//2,inW+MSIZE//2) :
            # 각 점을 처리
            s = 0.0
            for m in range(0 ,MSIZE) :
                for n in range(0,MSIZE) :
                    s += mask[m][n]*tmpInImage[i+m-MSIZE//2][k+n-MSIZE//2] # 마스크와 영상과 자리 맞추기
            tmpOutImage[i-MSIZE//2][k-MSIZE//2] = s

    # 127 더하기 (선택)
    for i in range(outH) :
        for k in range(outW) :
            tmpOutImage[i][k] += 127


    ## 임시 출력 --> 원 출력
    for i in range(outH) :
        for k in range(outW) :
            value = tmpOutImage[i][k]
            if value > 255 :
                value = 255
            elif value < 0 :
                value = 0
            outImage[i][k] = int(value)

    ## 출력
    displayImage()

# 저주파
def lowFrequencyImage() :
    alpha = askinteger("알파","값 -->",minvalue=1,maxvalue=30)
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    ## 중요! 코드, 출력영상 크기 결정##
    outH = inH
    outW = inW
    ###### 메모리 할당 ###########################
    outImage = []
    outImage = melloc(outH, outW)
    ###### 진짜 컴퓨터 비전 알고리즘 #####
    MSIZE = 3
    mask = [ [1/9, 1/9, 1/9],
             [1/9, 1/9, 1/9],
             [1/9, 1/9, 1/9] ]

    ## 임시 입력영상 메모리 확보
    tmpInImage = melloc(inH + MSIZE -1, inW + MSIZE -1, 127)  #127 중간값
    tmpOutImage = melloc(outH, outW)
    ## 원 입력 ---> 임시 입력
    for i in range(inH) :
        for k in range(inW) :
            tmpInImage[i+MSIZE//2][k+MSIZE//2] = inImage[i][k]
    ## 회선연산 : (1,1)이 중심
    for i in range(MSIZE//2,inH+MSIZE//2) :
        for k in range(MSIZE//2,inW+MSIZE//2) :
            # 각 점을 처리
            s = 0.0
            for m in range(0 ,MSIZE) :
                for n in range(0,MSIZE) :
                    s += mask[m][n]*tmpInImage[i+m-MSIZE//2][k+n-MSIZE//2] # 마스크와 영상과 자리 맞추기
            tmpOutImage[i-MSIZE//2][k-MSIZE//2] = s

    temp = [[num for num in range(outW)] for num in range(outH)]
    print(temp)
    for i in range(outH):
        for k in range(outW):
            temp[i][k] = alpha
        print(temp)

    for i in range(MSIZE//2,inH+MSIZE//2) :
        for k in range(MSIZE//2,inW+MSIZE//2) :
            tmpOutImage[i][k] = (temp[i][k] * tmpInImage[i+m-MSIZE//2][k+n-MSIZE//2]) - tmpOutImage[i][k]
    print(tmpOutImage)

    ## 임시 출력 --> 원 출력
    for i in range(outH) :
        for k in range(outW) :
            value = tmpOutImage[i][k]
            if value > 255 :
                value = 255
            elif value < 0 :
                value = 0
            outImage[i][k] = int(value)


    ## 출력
    displayImage()

#########################
#### 전역변수 선언부 ####
#########################
inImage,outImage = [],[]
inW, inH, outW, outH = [0]*4
window, canvas, paper = None, None, None
filename = ""
panYN = False
sx,sy,ex,ey = [0] * 4

# 경계선 검출
def boundaryImage() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    ## 중요! 코드, 출력영상 크기 결정##
    outH = inH
    outW = inW
    ###### 메모리 할당 ###########################
    outImage = []
    outImage = melloc(outH, outW)
    ###### 진짜 컴퓨터 비전 알고리즘 #####
    MSIZE = 3
    # 수직 에지 검출 마스크
    # mask = [ [0, 0, 0],
    #          [-1, 1, 0],
    #          [0, 0, 0] ]
    #
    # 수평 에지 검출 마스크
    mask = [ [0, -1, 0],
             [0, 1, 0],
             [0, 0, 0] ]

    ## 임시 입력영상 메모리 확보
    tmpInImage = melloc(inH + MSIZE -1, inW + MSIZE -1, 127)  #127 중간값
    tmpOutImage = melloc(outH, outW)
    ## 원 입력 ---> 임시 입력
    for i in range(inH) :
        for k in range(inW) :
            tmpInImage[i+MSIZE//2][k+MSIZE//2] = inImage[i][k]
    ## 회선연산 : (1,1)이 중심
    for i in range(MSIZE//2,inH+MSIZE//2) :
        for k in range(MSIZE//2,inW+MSIZE//2) :
            # 각 점을 처리
            s = 0.0
            for m in range(0 ,MSIZE) :
                for n in range(0,MSIZE) :
                    s += mask[m][n]*tmpInImage[i+m-MSIZE//2][k+n-MSIZE//2] # 마스크와 영상과 자리 맞추기
            tmpOutImage[i-MSIZE//2][k-MSIZE//2] = s

    # 127 더하기 (선택)
    for i in range(outH) :
        for k in range(outW) :
            tmpOutImage[i][k] += 127

    ## 임시 출력 --> 원 출력
    for i in range(outH) :
        for k in range(outW) :
            value = tmpOutImage[i][k]
            if value > 255 :
                value = 255
            elif value < 0 :
                value = 0
            outImage[i][k] = int(value)

    ## 출력
    displayImage()

#####################
#### 메인 코드부 ####
#####################
window = Tk()
window.title('컴퓨터 비젼(딥러닝 기법) ver 0.03')
window.geometry("500x500")


mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label='파일', menu=fileMenu)
fileMenu.add_command(label='파일 열기', command=openImage)
fileMenu.add_separator()
fileMenu.add_command(label='파일 저장', command=saveImage)

comVisionMenu1 = Menu(mainMenu)
mainMenu.add_cascade(label='화소점 처리', menu=comVisionMenu1)
comVisionMenu1.add_command(label='밝게하기', command=addImage)
comVisionMenu1.add_command(label='어둡게하기', command=minusImage)
comVisionMenu1.add_command(label='영상 곱셈', command=multiplyImage)
comVisionMenu1.add_command(label='영상 나눗셈', command=divisionImage)
comVisionMenu1.add_command(label='화소값 반전', command=reversedImage)
comVisionMenu1.add_command(label='입출력 영상 평균값', command=averageImage)
comVisionMenu1.add_command(label='파라볼라', command=paraImage)


comVisionMenu2 = Menu(mainMenu)
mainMenu.add_cascade(label='통계', menu=comVisionMenu2 )
comVisionMenu2.add_command(label='이진화', command=binaryImage)
comVisionMenu2.add_command(label='축소(평균변환)', command=zoomOutImage2)
comVisionMenu2.add_command(label='확대(양선형보간변환)', command=zoomInImage2)
comVisionMenu2.add_separator()
comVisionMenu2.add_command(label='히스토그램', command=histoImage)
comVisionMenu2.add_command(label='명암대비', command=stretchImage)
comVisionMenu2.add_command(label='End-In탐색', command=endinImage)
comVisionMenu2.add_command(label='히스토그램 평활화', command=histoEqualImage)

comVisionMenu3 = Menu(mainMenu)
mainMenu.add_cascade(label='기하학 처리', menu=comVisionMenu3)
comVisionMenu3.add_command(label='상하반전', command=upDownImage)
comVisionMenu3.add_command(label='오른쪽 90도 회전', command=rotationImage)
comVisionMenu3.add_command(label='축소', command=zoomOutImage)
comVisionMenu3.add_command(label='확대', command=zoomInImage)
comVisionMenu3.add_command(label='이동', command=moveImage)
comVisionMenu3.add_command(label='회전1', command=rotateImage)
comVisionMenu3.add_command(label='회전2', command=rotateImage2)


comVisionMenu4 = Menu(mainMenu)
mainMenu.add_cascade(label='화소영역 처리', menu=comVisionMenu4)
comVisionMenu4.add_command(label='엠보싱', command=embossImage)
comVisionMenu4.add_command(label='블러링', command=blurImage)
comVisionMenu4.add_command(label='샤프닝', command=sharpImage)
comVisionMenu4.add_command(label='경계선 검출', command=boundaryImage)
comVisionMenu4.add_command(label='가우시안 필터링', command=gaussianImage)
comVisionMenu4.add_command(label='고주파', command=highFrequencyImage)
comVisionMenu4.add_command(label='저주파', command=lowFrequencyImage)

window.mainloop()