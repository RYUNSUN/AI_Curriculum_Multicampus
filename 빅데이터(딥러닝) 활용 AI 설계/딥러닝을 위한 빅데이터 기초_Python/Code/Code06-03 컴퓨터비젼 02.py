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
def melloc(h,w) :
    retMemory = []
    for _ in range(h) :
        tmpList=[]
        for _ in range(w) :
            tmpList.append(0)
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
    loadImage(filename)
    eqaulImage()


def saveImage() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    pass

def displayImage() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    if canvas!= None : # 예전에 실행한 적이 있다.
        canvas.destroy() # 캔버스를 뜯어내는 것
    ## 화면 크기를 조절
    window.geometry(str(outH) + 'x' + str(outW)) # 벽
    canvas = Canvas(window, height = outH, width = outW) # 보드
    paper = PhotoImage(height = outH, width = outW) # 빈 종이
    canvas.create_image((outH//2, outW//2), image=paper, state='normal') # state는 보통 normal 씀
    ## 출력영상 ---> 화면에 한점씩 찍자
    for i in range(outH) :
        for k in range(outW) :
            r = g = b = outImage[i][k]
            paper.put("#%02x%02x%02x" % (r, g, b),(k, i)) # RRGGBB 16진수로 표현한 것, x는 16진수

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
def updownMoveImage(event) :
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
    if event == 1 :
        for i in range(inH) :
            for k in range(inW) :
                if i - value > 0 :
                    outImage[i-value][k] = inImage[i][k]
    elif event == 2 :
        for i in range(inH) :
            for k in range(inW) :
                if i - value > 0 :
                    outImage[i][k] = inImage[i-value][k]
    elif event == 3 :
        for i in range(inH) :
            for k in range(inW) :
                if k - value > 0 :
                    outImage[i][k-value] = inImage[i][k]
    else :
        for i in range(inH) :
            for k in range(inW) :
                if k - value > 0 :
                    outImage[i][k] = inImage[i][k-value]

    ## 출력
    displayImage()


#########################
#### 전역변수 선언부 ####
#########################
inImage,outImage = [],[]
inW, inH, outW, outH = [0]*4
window, canvas, paper = None, None, None
filename = ""


#####################
#### 메인 코드부 ####
#####################
window = Tk()
window.title('컴퓨터 비젼(딥러닝 기법) ve 0.02')
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
mainMenu.add_cascade(label='화소(통계)', menu=comVisionMenu2 )
comVisionMenu2.add_command(label='이진화', command=binaryImage)

comVisionMenu3 = Menu(mainMenu)
mainMenu.add_cascade(label='기하학 처리', menu=comVisionMenu3)
comVisionMenu3.add_command(label='상하반전', command=upDownImage)
comVisionMenu3.add_command(label='오른쪽 90도 회전', command=rotationImage)

conVisionMenu4 = Menu(comVisionMenu3)
comVisionMenu3.add_cascade(label='이동', menu=conVisionMenu4)
conVisionMenu4.add_command(label='위', command=lambda  : updownMoveImage(1))
conVisionMenu4.add_command(label='아래', command=lambda  : updownMoveImage(2))
conVisionMenu4.add_command(label='좌', command=lambda  : updownMoveImage(3))
conVisionMenu4.add_command(label='우', command=lambda  : updownMoveImage(4))
window.mainloop()