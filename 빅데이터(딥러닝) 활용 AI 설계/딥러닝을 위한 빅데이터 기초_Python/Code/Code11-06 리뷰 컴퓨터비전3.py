from tkinter import *
from tkinter.simpledialog import *
from tkinter.filedialog import *
import math
import os
import os.path
from tkinter import messagebox
import numpy as np

# 메모리를 할당해서 리스트(참조)를 반환하는 함수
def melloc(h, w, dataType = np.uint8):  # initValue : defualt parameter function (초기값 설정하기 위해) , uint8:0~255
    retMemory = []
    retMemory = np.zeros((h,w), dtype=dataType)
    print(retMemory)
    retMemory.shape
    return retMemory


# 파일을 메모리로 로딩하는 함수
def loadImage(fname):
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    fsize = os.path.getsize(fname)  # 파일의 크기(바이트)
    inH = inW = int(math.sqrt(fsize))  # 핵심 코드 (메모리를 확보하기 위한 파일의 크기 확인)

    ## 입력영상 메모리 확보 ##
    inImage = []  # 이미지가 누적되지 않고 새롭게 불러올 수 있도록 초기화
    inImage = melloc(inH, inW)

    # 파일 --> 메모리
    with open(fname, 'rb') as rFp:  # 파일 선택
        for i in range(inH):
            for k in range(inW):
                inImage[i][k] = int(ord(rFp.read(1)))  # 1바이트씩 읽힘, ord : 문자의 아스키 값 반환


def openImage():
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    filename = askopenfilename(parent=window, filetypes=(("RAW 파일", "*.raw"), ("모든파일", "*.*")))
    if filename == '' or filename == None:
        return

    loadImage(filename)
    eqaulImage()


def displayImage():
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    global VIEW_X, VIEW_Y
    if canvas != None:  # 캔버스가 누적되므로 이를 방지하기 위해 예전에 실행한 적이 있는지 물어보는 것.
        canvas.destroy()  # 캔버스를 뜯어내는 것

    ## 고정된 화면 크기
    if outH <= VIEW_Y or outW <= VIEW_X:  # 512x512 보다 작으면 그냥 출력
        VIEW_X = outW
        VIEW_Y = outH
        step = 1  # 출력시 건너뛸 값
    else:  # 512x512 보다 크면 최대 512까지 보이게 하기 위해 건너뛰어 출력하도록 하는 것
        VIEW_X = 512
        VIEW_Y = 512
        step = outW / VIEW_X  # 맞아떨어지지 않은 값은 실수로 출력

    window.geometry(str(int(VIEW_Y * 1.2)) + 'x' + str(int(VIEW_X * 1.2)))  # 좀 더 이쁘게 보이기 위해 갭 준것 x1.2
    canvas = Canvas(window, height=VIEW_Y, width=VIEW_X)
    paper = PhotoImage(height=VIEW_Y, width=VIEW_X)  # 빈 종이
    canvas.create_image((VIEW_Y // 2, VIEW_X // 2), image=paper, state='normal')

    ## 성능 개선
    # 한칸씩 찍으면 오래 걸리므로 문자열로 한 줄씩 출력하는 코드
    import numpy
    rgbStr = ''  # 전체 픽셀의 문자열을 저장
    for i in numpy.arange(0, outH, step):  # numpy는 실수값도 범위로 설정 가능
        tmpStr = ''
        for k in numpy.arange(0, outW, step):
            i = int(i)
            k = int(k)
            r = g = b = outImage[i][k]
            tmpStr += ' #%02x%02x%02x' % (r, g, b)  # 문자열은 한칸씩 띄기
        rgbStr += '{' + tmpStr + '} '  # 마지막 중괄호 뒤에 한칸 띄기
    paper.put(rgbStr)

    canvas.pack(expand=1, anchor=CENTER)
    status.configure(text='이미지 정보 :' + str(outW) + 'x' + str(outH))


#############################################
####컴퓨터 비전(영상처리) 알고리즘 함수 모음 ####
#############################################
# 동일영상 알고리즘
def eqaulImage():
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    ## 중요! 코드, 출력영상 크기 결정##
    # outImage는 알고리즘에 따라 크기가 달라질 수 있음(예.확대, 축소)
    outH = inH
    outW = inW
    ###### 메모리 할당 ###########################
    outImage = inImage[:] # inImage 복사
    displayImage()  # 사람 눈에 보이게 출력하기 위한 함수

# 화소점 처리 (밝게하기)
def addImage():
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    ## 중요! 코드, 출력영상 크기 결정##
    # outImage는 알고리즘에 따라 크기가 달라질 수 있음(예.확대, 축소)
    outH = inH
    outW = inW
    ###### 메모리 할당 ###########################
    outImage = inImage + 100
    displayImage()  # 사람 눈에 보이게 출력하기 위한 함수

#########################
#### 전역변수 선언부 ####
#########################
inImage,outImage = [],[]
inW, inH, outW, outH = [0]*4
window, canvas, paper = None, None, None
filename = ""
VIEW_X, VIEW_Y = 512,512 #화면에 보일 크기 (출력용)


#####################
#### 메인 코드부 ####
#####################
window = Tk()
window.title('리뷰용 컴퓨터 비전')
window.geometry("500x500")

status = Label(window, text = '이미지 정보',bd = 1 , relief = SUNKEN, anchor = W) # 창의 밑에 붙는 것
status.pack(side = BOTTOM,fill=X)

mainMenu = Menu(window)
window.config(menu=mainMenu)
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label='파일', menu=fileMenu)
fileMenu.add_command(label='파일 열기', command=openImage) # command = 함수 -> 콜백함수, 뒤에 ()를 실행한다는 의미로 붙이면 X,

cvMenu = Menu(mainMenu)
mainMenu.add_cascade(label='컴퓨터비전', menu=cvMenu)
cvMenu.add_command(label='밝게하기', command=addImage) # command = 함수 -> 콜백함수, 뒤에 ()를 실행한다는 의미로 붙이면 X,

window.mainloop()