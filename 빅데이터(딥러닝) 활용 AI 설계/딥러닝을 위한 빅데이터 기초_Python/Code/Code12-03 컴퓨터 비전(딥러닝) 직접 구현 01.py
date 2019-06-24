from tkinter import *
from tkinter.simpledialog import *
from tkinter.filedialog import *
import math
import os
import os.path
from tkinter import messagebox
from PIL import Image, ImageFilter, ImageEnhance, ImageOps

# 메모리를 할당해서 리스트(참조)를 반환하는 함수
def malloc(h,w,initValue=0) :
    retMemory = []
    for _ in range(h) :
        tmpList=[]
        for _ in range(w) :
            tmpList.append(initValue)
        retMemory.append(tmpList)
    return retMemory

# 파일을 메모리로 로딩하는 함수
def loadImageColor(fname) :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    inImage=[]
    photo = Image.open(fname) # PIL 객체
    inW = photo.width
    inH = photo.height
    ## 메모리 확보 ##
    for _ in range(3):
        inImage.append(malloc(inH,inW))

    photoRGB = photo.convert('RGB')
    for i in range(inH) :
        for k in range(inW) :
            r, g, b = photoRGB.getpixel((k,i))
            inImage[R][i][k] = r
            inImage[G][i][k] = g
            inImage[B][i][k] = b

# 파일을 선택해서 메모리로 로딩하는 함수
def openImageColor() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    filename = askopenfilename(parent=window,filetypes=(("칼라 파일", "*.jpg;*.png;*.bmp;*.tif"), ("모든파일", "*.*")))
    if filename == '' or filename == None :
        return
    loadImageColor(filename)
    equalImageColor()

    displayImageColor()

def displayImageColor() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    if canvas!= None : # 예전에 실행한 적이 있다.
        canvas.destroy() # 캔버스를 뜯어내는 것
    VIEW_X = outW
    VIEW_Y = outH
    step = 1

    window.geometry(str(int(VIEW_X*1.2)) + 'x' + str(int(VIEW_Y*1.2))) # 좀 더 이쁘게 보이기 위해 x1.2
    canvas = Canvas(window, height=VIEW_Y, width=VIEW_X)
    paper = PhotoImage(height=VIEW_Y, width=VIEW_X)  # 빈 종이
    canvas.create_image((VIEW_X // 2, VIEW_Y // 2), image=paper, state='normal')

    import numpy
    rgbStr = '' #전체 픽셀의 문자열을 저장
    for i in numpy.arange(0,outH,step) : #numpy는 실수값도 범위로 설정 가능
        tmpStr = ''
        for k in numpy.arange(0,outW,step) :
            i = int(i)
            k = int(k)
            r, g, b = outImage[R][i][k], outImage[G][i][k], outImage[B][i][k]
            tmpStr += ' #%02x%02x%02x' % (r,g,b) # 문자열은 한칸씩 띄기
        rgbStr += '{' + tmpStr + '} ' # 마지막 중괄호 뒤에 한칸 띄기
    paper.put(rgbStr)

    ## 마우스 이벤트
    canvas.bind("<Button-1>", mouseClick)
    canvas.bind("<ButtonRelease-1>",mouseDrop)
    canvas.pack(expand=1,anchor=CENTER)
    status.configure(text = '이미지 정보 :' + str(outW) + 'x' + str(outH))


def saveImageColor() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    # if outImage == None :
    #     return
    # saveFp = asksaveasfile(parent=window, mode='wb', defaultextension='*.jpg'
    #                            , filetypes=(("JPG 파일", "*.jpg"), ("모든파일", "*.*")))
    # if saveFp == '' or saveFp == None:
    #     return
    # outImage.save(saveFp.name)
    # print('Save~')

# 동일영상 알고리즘
def equalImageColor() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    ## 중요! 코드, 출력영상 크기 결정##
    outH = inH
    outW = inW
    ## 메모리 할당 ##
    outImage = []
    for _ in range(3):
        outImage.append(malloc(outH,outW))
    ##############################
    ### 진짜 컴퓨터 비전 알고리즘 ###
    ##############################
    for RGB in range(3):
        for i in range(inH):
            for k in range(inW):
                outImage[RGB][i][k] = inImage[RGB][i][k]
    ######################################

    displayImageColor()


def addImageColor() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    ## 중요! 코드, 출력영상 크기 결정##
    outH = inH
    outW = inW
    ## 메모리 할당 ##
    outImage = []
    for _ in range(3):
        outImage.append(malloc(outH,outW))
    ##############################
    ### 진짜 컴퓨터 비전 알고리즘 ###
    ##############################
    value = askinteger("밝게/어둡게","값( -->",minvalue=-255,maxvalue=255)
    for RGB in range(3):
        for i in range(inH):
            for k in range(inW):
                if inImage[RGB][i][k] + value > 255:
                    outImage[RGB][i][k] = 255
                elif inImage[RGB][i][k] + value < 0:
                    outImage[RGB][i][k] = 0
                else :
                    outImage[RGB][i][k] = inImage[RGB][i][k] + value
    ######################################

    displayImageColor()

def revImageColor() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    ## 중요! 코드, 출력영상 크기 결정##
    outH = inH
    outW = inW
    ## 메모리 할당 ##
    outImage = []
    for _ in range(3):
        outImage.append(malloc(outH,outW))
    ##############################
    ### 진짜 컴퓨터 비전 알고리즘 ###
    ##############################
    for RGB in range(3):
        for i in range(inH):
            for k in range(inW):
                outImage[RGB][i][k] = 255-inImage[RGB][i][k]
    ######################################

    displayImageColor()

def paraImageColor():
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    ## 중요! 코드, 출력영상 크기 결정##
    outH = inH
    outW = inW
    ## 메모리 할당 ##
    outImage = []
    for _ in range(3):
        outImage.append(malloc(outH,outW))
    ##############################
    ### 진짜 컴퓨터 비전 알고리즘 ###
    ##############################
    LUT = [0 for _ in range(256)]
    for input in range(256) :
        LUT[input] = int(255 - 255 * math.pow(input / 128 - 1, 2))

    for RGB in range(3):
        for i in range(inH):
            for k in range(inW):
                outImage[RGB][i][k] = LUT[inImage[RGB][i][k]]
    ######################################

    displayImageColor()

def morphImageColor():
    global window, canvas, paper, filename, inImage, outImage, inH, inW, outH, outW
    ## 중요! 코드. 출력영상 크기 결정 ##
    outH = inH;
    outW = inW;
    ## 메모리 확보
    outImage = []
    for _ in range(3):
        outImage.append(malloc(outH, outW))
    ############################
    ### 진짜 컴퓨터 비전 알고리즘 ###\
    LUT = [0 for _ in range(256)]
    for input in range(256):
        LUT[input] = int(255 - 255 * math.pow(input / 128 - 1, 2))

    for RGB in range(3):
        for i in range(inH):
            for k in range(inW):
                outImage[RGB][i][k] = LUT[inImage[RGB][i][k]]
    #############################
    displayImageColor()


def morphImageColor():
    global window, canvas, paper, filename, inImage, outImage, inH, inW, outH, outW
    ## 중요! 코드. 출력영상 크기 결정 ##
    outH = inH;
    outW = inW;
    ## 추가 영상 선택
    filename2 = askopenfilename(parent=window,
                                filetypes=(("칼라 파일", "*.jpg;*.png;*.bmp;*.tif"), ("모든 파일", "*.*")))
    if filename2 == '' or filename2 == None:
        return
    inImage2 = []
    photo2 = Image.open(filename2)  # PIL 객체
    inW2 = photo2.width;
    inH2 = photo2.height
    ## 메모리 확보
    for _ in range(3):
        inImage2.append(malloc(inH2, inW2))

    photoRGB2 = photo2.convert('RGB')
    for i in range(inH2):
        for k in range(inW2):
            r, g, b = photoRGB2.getpixel((k, i))
            inImage2[R][i][k] = r
            inImage2[G][i][k] = g
            inImage2[B][i][k] = b

    ## 메모리 확보
    outImage = []
    for _ in range(3):
        outImage.append(malloc(outH, outW))

    import threading
    import time
    def morpFunc():
        w1 = 1;
        w2 = 0
        for _ in range(20):
            for RGB in range(3):
                for i in range(inH):
                    for k in range(inW):
                        newValue = int(inImage[RGB][i][k] * w1 + inImage2[RGB][i][k] * w2)
                        if newValue > 255:
                            newValue = 255
                        elif newValue < 0:
                            newValue = 0
                        outImage[RGB][i][k] = newValue
            displayImageColor()
            w1 -= 0.05;
            w2 += 0.05
            time.sleep(0.5)

    threading.Thread(target=morpFunc).start()

# 상하반전 알고리즘
def upDownImageColor() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    ## 중요! 코드, 출력영상 크기 결정##
    outH = inH
    outW = inW
    ###### 메모리 할당 ###########################
    outImage = []
    for _ in range(3):
        outImage.append(malloc(outH, outW))
    ###### 진짜 컴퓨터 비전 알고리즘 #####
    for RGB in range(3) :
        for i in range(inH) :
            for k in range(inW) :
                outImage[RGB][inH-i-1][k] = inImage[RGB][i][k]

    displayImageColor()

# 영상 축소 알고리즘
def zoomOutImageColor() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    scale = askinteger("축소","값 -->",minvalue=2,maxvalue=16)
    ## 중요! 코드, 출력영상 크기 결정##
    outH = inH//scale
    outW = inW//scale
    ###### 메모리 할당 ###########################
    outImage = []
    for _ in range(3):
        outImage.append(malloc(outH, outW))
    ###### 진짜 컴퓨터 비전 알고리즘 #####
    for RGB in range(3) :
        for i in range(outH) :
            for k in range(outW) :
                outImage[RGB][i][k] = inImage[RGB][i*scale][k*scale]

    displayImageColor()

# 영상 확대 알고리즘
def zoomInImageColor() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    scale = askinteger("확대","값 -->",minvalue=2,maxvalue=4)
    ## 중요! 코드, 출력영상 크기 결정##
    outH = inH*scale
    outW = inW*scale
    ###### 메모리 할당 ###########################
    outImage = []
    for _ in range(3):
        outImage.append(malloc(outH, outW))
    ###### 진짜 컴퓨터 비전 알고리즘 #####
    for RGB in range(3) :
        for i in range(outH) :
            for k in range(outW) :
                outImage[RGB][i][k] = inImage[RGB][i//scale][k//scale]

    displayImageColor()

## 마우스 화면이동 알고리즘
def moveImageColor() :
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
    for _ in range(3):
        outImage.append(malloc(outH, outW))
    ###### 진짜 컴퓨터 비전 알고리즘 #####
    mx = sx - ex
    my = sy - ey
    for RGB in range(3) :
        for i in range(inH) :
            for k in range(inW) :
                if 0 <= i-my < outH and 0 <= k-mx < outW :
                    outImage[RGB][i-my][k-mx] = inImage[RGB][i][k]
    panYN = False
    ## 출력
    displayImageColor()

# 화소점 처리 알고리즘(이진화)
def binaryImageColor() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    ## 중요! 코드, 출력영상 크기 결정##
    outH = inH
    outW = inW
    ###### 메모리 할당 ###########################
    outImage = []
    for _ in range(3):
        outImage.append(malloc(outH, outW))
    ###### 진짜 컴퓨터 비전 알고리즘 #####
    ##영상의 평균 구하기
    grayImage = []
    tmp = []
    sum = 0

    for i in range(inH) :
        tmp = []
        for k in range(inW) :
            gray = int((inImage[R][i][k]+inImage[G][i][k]+inImage[B][i][k])//3)
            if gray > 255 :
                gray = 255
            elif gray < 0 :
                gray = 0
            else :
                gray = gray
            sum += gray
            tmp.append(gray)
        grayImage.append(tmp)
    avg = sum // (inW * inH)

    for RGB in range(3) :
        outImage[RGB] = grayImage

    for GRB in range(3) :
        for i in range(inH) :
            for k in range(inW) :
                if outImage[RGB][i][k] > avg :
                    outImage[RGB][i][k] = 255
                else :
                    outImage[RGB][i][k] = 0

    displayImageColor()

# 오른쪽 90도 회전 알고리즘
def rotationImageColor() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    ## 중요! 코드, 출력영상 크기 결정##
    outH = inH
    outW = inW
    ###### 메모리 할당 ###########################
    outImage = []
    for _ in range(3):
        outImage.append(malloc(outH, outW))
    ###### 진짜 컴퓨터 비전 알고리즘 #####
    for RGB in range(3) :
        for i in range(inH) :
            for k in range(inW) :
                outImage[RGB][k][inW-i-1] = inImage[RGB][i][k]
    ## 출력
    displayImageColor()

# 영상 회전 알고리즘
def rotateImageColor() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    angle = askinteger("회전","값 -->",minvalue=1,maxvalue=360)
    ## 중요! 코드, 출력영상 크기 결정##
    outH = inH
    outW = inW
    ###### 메모리 할당 ###########################
    outImage = []
    for _ in range(3):
        outImage.append(malloc(outH, outW))
    ###### 진짜 컴퓨터 비전 알고리즘 #####
    radian = angle * math.pi / 180 # radian degree 수식
    for RGB in range(3):
        for i in range(inH) :
            for k in range(inW) :
                xs = i
                ys = k
                xd = int(math.cos(radian) * xs - math.sin(radian) * ys)
                yd = int(math.sin(radian) * xs + math.cos(radian) * ys)
                if 0<= xd < inH and 0 <= yd < inW :
                    outImage[RGB][xd][yd] = inImage[RGB][i][k]

    displayImageColor()

# 영상 회전 알고리즘
def rotateImageColor2() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    angle = askinteger("회전","값 -->",minvalue=1,maxvalue=360)
    ## 중요! 코드, 출력영상 크기 결정##
    outH = inH
    outW = inW
    ###### 메모리 할당 ###########################
    outImage = []
    for _ in range(3):
        outImage.append(malloc(outH, outW))
    ###### 진짜 컴퓨터 비전 알고리즘 #####
    radian = angle * math.pi / 180
    cx = inW // 2;
    cy = inH // 2
    for RGB in range(3):
        for i in range(outH):
            for k in range(outW):
                xs = i;
                ys = k;
                xd = int(math.cos(radian) * (xs - cx) - math.sin(radian) * (ys - cy)) + cx
                yd = int(math.sin(radian) * (xs - cx) + math.cos(radian) * (ys - cy)) + cy
                if 0 <= xd < outH and 0 <= yd < outW:
                    outImage[RGB][xs][ys] = inImage[RGB][xd][yd]
                else:
                    outImage[RGB][xs][ys] = 255

    displayImageColor()

# 엠보싱 처리
def embossImageColor() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    ## 중요! 코드, 출력영상 크기 결정##
    outH = inH
    outW = inW
    ###### 메모리 할당 ###########################
    outImage = []
    for _ in range(3):
        outImage.append(malloc(outH, outW))
    ###### 진짜 컴퓨터 비전 알고리즘 #####
    MSIZE = 3
    mask = [ [-1, 0, 0],
             [ 0, 0, 0],
             [ 0, 0, 1] ]
    ## 임시 입력영상 메모리 확보
    tmpInImage = []
    for _ in range(3):
        tmpInImage.append(malloc(inH + MSIZE -1, inW + MSIZE -1, 127))
    tmpOutImage = []
    for _ in range(3):
        tmpOutImage .append(malloc(outH, outW))

    ## 원 입력 ---> 임시 입력
    for RGB in range(3):
        for i in range(inH) :
            for k in range(inW) :
                tmpInImage[RGB][i+MSIZE//2][k+MSIZE//2] = inImage[RGB][i][k]
    ## 회선연산 : (1,1)이 중심
    for RGB in range(3):
        for i in range(MSIZE//2,inH+MSIZE//2) :
            for k in range(MSIZE//2,inW+MSIZE//2) :
                # 각 점을 처리
                s = 0.0
                for m in range(0 ,MSIZE) :
                    for n in range(0,MSIZE) :
                        s += mask[m][n]*tmpInImage[RGB][i+m-MSIZE//2][k+n-MSIZE//2] # 마스크와 영상과 자리 맞추기
                tmpOutImage[RGB][i-MSIZE//2][k-MSIZE//2] = s

    ## 127 더하기 (선택)
    for RGB in range(3):
        for i in range(outH) :
            for k in range(outW) :
                tmpOutImage[RGB][i][k] += 127

    ## 임시 출력 --> 원 출력
    for RGB in range(3):
        for i in range(outH) :
            for k in range(outW) :
                value = tmpOutImage[RGB][i][k]
                if value > 255 :
                    value = 255
                elif value < 0 :
                    value = 0
                outImage[RGB][i][k] = int(value)


    ## 출력
    displayImageColor()

# 히스토그램
import matplotlib.pyplot as plt
def histoImageColor() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    rCountList = [0] * 256
    gCountList =[0] * 256
    bCountList = [0] * 256

    for i in range(inH) :
        for k in range(inW) :
            rCountList[inImage[R][i][k]] += 1

    for i in range(outH) :
        for k in range(outW) :
            gCountList[inImage[G][i][k]] += 1

    for i in range(outH) :
        for k in range(outW) :
            bCountList[inImage[B][i][k]] += 1

    plt.plot(rCountList)
    plt.plot(gCountList)
    plt.plot(bCountList)
    plt.show()

#######################
#### 전역변수 선언부 ####
#######################
R, G, B = 0,1,2
inImage,outImage = [],[] # 3차원 리스트(배열)
inW, inH, outW, outH = [0]*4
window, canvas, paper = None, None, None
filename = ""
VIEW_X, VIEW_Y = 512,512 #화면에 보일 크기 (출력용)


####################
#### 메인 코드부 ####
####################
window = Tk()
window.title('컴퓨터 비젼 칼라(딥러닝) ver 0.01')
window.geometry("500x500")

status = Label(window, text = '이미지 정보:',bd = 1 , relief = SUNKEN, anchor = W)
status.pack(side = BOTTOM,fill=X)

mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label='파일', menu=fileMenu)
fileMenu.add_command(label='파일 열기', command=openImageColor)
fileMenu.add_separator()
fileMenu.add_command(label='파일 저장', command=saveImageColor)

comVisionMenu1 = Menu(mainMenu)
mainMenu.add_cascade(label='화소점 처리', menu=comVisionMenu1)
comVisionMenu1.add_command(label='덧셈/뺄셈', command=addImageColor)
comVisionMenu1.add_command(label='화소값 반전', command=revImageColor)
comVisionMenu1.add_command(label='파라볼라', command=paraImageColor)
fileMenu.add_separator()
comVisionMenu1.add_command(label='모핑', command=morphImageColor)

comVisionMenu2 = Menu(mainMenu)
mainMenu.add_cascade(label='통계', menu=comVisionMenu2 )
comVisionMenu2.add_command(label='이진화', command=binaryImageColor)
# comVisionMenu2.add_command(label='축소(평균변환)', command=zoomOutImage2)
# comVisionMenu2.add_command(label='확대(양선형보간변환)', command=zoomInImage2)
# comVisionMenu2.add_separator()
comVisionMenu2.add_command(label='히스토그램', command=histoImageColor)
comVisionMenu2.add_command(label='히스토그램(내꺼)', command=histoImageColor2)
# comVisionMenu2.add_command(label='명암대비', command=stretchImage)
# comVisionMenu2.add_command(label='End-In탐색', command=endinImage)
# comVisionMenu2.add_command(label='히스토그램 평활화', command=histoEqualImage)

comVisionMenu3 = Menu(mainMenu)
mainMenu.add_cascade(label='기하학 처리', menu=comVisionMenu3)
comVisionMenu3.add_command(label='상하반전', command=upDownImageColor)
comVisionMenu3.add_command(label='오른쪽 90도 회전', command=rotationImageColor)
comVisionMenu3.add_command(label='축소', command=zoomOutImageColor)
comVisionMenu3.add_command(label='확대', command=zoomInImageColor)
comVisionMenu3.add_command(label='이동', command=moveImageColor)
comVisionMenu3.add_command(label='회전1', command=rotateImageColor)
comVisionMenu3.add_command(label='회전2(중심, 역방향)', command=rotateImageColor2)


comVisionMenu4 = Menu(mainMenu)
mainMenu.add_cascade(label='화소영역 처리', menu=comVisionMenu4)
comVisionMenu4.add_command(label='엠보싱', command=embossImageColor)
# comVisionMenu4.add_command(label='블러링', command=blurImage)
# comVisionMenu4.add_command(label='샤프닝', command=sharpImage)
# comVisionMenu4.add_command(label='경계선 검출', command=boundaryImage)
# comVisionMenu4.add_command(label='가우시안 필터링', command=gaussianImage)
# comVisionMenu4.add_command(label='고주파', command=highFrequencyImage)
# comVisionMenu4.add_command(label='저주파', command=lowFrequencyImage)

# comVisionMenu5 = Menu(mainMenu)
# mainMenu.add_cascade(label='데이터베이스 입출력', menu=comVisionMenu5)
# comVisionMenu5.add_command(label='MySQL에서 불러오기', command=loadMysql)
# comVisionMenu5.add_command(label='MySQL에 저장하기', command=saveMysql)
# comVisionMenu5.add_separator()
# comVisionMenu5.add_command(label='CSV 열기', command=openCSV)
# comVisionMenu5.add_command(label='CSV 형식으로 저장', command=saveCSV)
# comVisionMenu5.add_separator()
# comVisionMenu5.add_command(label='엑셀 열기', command=openExcel)
# comVisionMenu5.add_command(label='엑셀 형식으로 저장', command=saveExcel)
# comVisionMenu5.add_command(label='엑셀 아트로 저장', command=saveExcelArt)

window.mainloop()