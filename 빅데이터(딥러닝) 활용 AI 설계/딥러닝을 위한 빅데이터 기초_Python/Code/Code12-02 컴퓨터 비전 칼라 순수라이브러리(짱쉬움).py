from tkinter import *
from tkinter.simpledialog import *
from tkinter.filedialog import *
import math
import os
import os.path
from tkinter import messagebox
from PIL import Image, ImageFilter, ImageEnhance, ImageOps

# 파일을 선택해서 메모리로 로딩하는 함수
import time
def openImagePIL() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    filename = askopenfilename(parent=window,filetypes=(("칼라 파일", "*.jpg;*.png;*.bmp;*.tif"), ("모든파일", "*.*")))
    if filename == '' or filename == None :
        return

    inImage = Image.open(filename)
    inW = inImage.width
    inH = inImage.height

    outImage = inImage.copy()
    outW = outImage.width
    outH = outImage.height

    displayImagePIL()

    # equalImage()

def displayImagePIL() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    if canvas!= None : # 예전에 실행한 적이 있다.
        canvas.destroy() # 캔버스를 뜯어내는 것
    VIEW_X = outW
    VIEW_Y = outH
    step = 1

    window.geometry(str(int(VIEW_Y*1.2)) + 'x' + str(int(VIEW_X*1.2))) # 좀 더 이쁘게 보이기 위해 x1.2
    canvas = Canvas(window, height=VIEW_Y, width=VIEW_X)
    paper = PhotoImage(height=VIEW_Y, width=VIEW_X)  # 빈 종이
    canvas.create_image((VIEW_Y // 2, VIEW_X // 2), image=paper, state='normal')

    import numpy
    rgbImage = outImage.convert('RGB') #rgb 형식으로 바꿔줌
    rgbStr = '' #전체 픽셀의 문자열을 저장
    for i in numpy.arange(0,outH,step) : #numpy는 실수값도 범위로 설정 가능
        tmpStr = ''
        for k in numpy.arange(0,outW,step) :
            i = int(i)
            k = int(k)
            r, g, b = rgbImage.getpixel((k,i))
            tmpStr += ' #%02x%02x%02x' % (r,g,b) # 문자열은 한칸씩 띄기
        rgbStr += '{' + tmpStr + '} ' # 마지막 중괄호 뒤에 한칸 띄기
    paper.put(rgbStr)

    canvas.pack(expand=1,anchor=CENTER)
    status.configure(text = '이미지 정보 :' + str(outW) + 'x' + str(outH))


def saveImagePIL() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    if outImage == None :
        return
    saveFp = asksaveasfile(parent=window, mode='wb', defaultextension='*.jpg'
                               , filetypes=(("JPG 파일", "*.jpg"), ("모든파일", "*.*")))
    if saveFp == '' or saveFp == None:
        return
    outImage.save(saveFp.name)
    print('Save~')

def addImagePIL() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    value = askfloat("밝게하기","값(0~16) -->",minvalue=0.0,maxvalue=16.0)
    outImage = inImage.copy()
    outImage = ImageEnhance.Brightness(outImage).enhance(value)
    outW = outImage.width
    outH = outImage.height
    displayImagePIL()

def blurImagePIL() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    outImage = inImage.copy()
    outImage = outImage.filter(ImageFilter.BLUR)
    outW = outImage.width
    outH = outImage.height
    displayImagePIL()

def zoominImagePIL():
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    scale = askinteger("확대", "값(0~8) -->", minvalue=2, maxvalue=8)
    outImage = inImage.copy()
    outImage = outImage.resize((inH*scale, inW*scale))
    outW = outImage.width
    outH = outImage.height
    displayImagePIL()

def zoomoutImagePIL():
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    scale = askinteger("축소", "값(2~8) -->", minvalue=2, maxvalue=8)
    outImage = inImage.copy()
    outImage = outImage.resize((inH//scale, inW//scale))
    outW = outImage.width
    outH = outImage.height
    displayImagePIL()

# def paraImagePIL() :
#     global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
#     value = askfloat("밝게하기","값(0~16) -->",minvalue=0.0,maxvalue=16.0)
#     outImage = inImage.copy()
#     outImage = ImageEnhance.Brightness(outImage).enhance(value)
#     outW = outImage.width
#     outH = outImage.height
#     displayImagePIL()

def rotateImagePIL() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    angle = askinteger("회전","값 -->",minvalue=1,maxvalue=360)
    outImage = inImage.copy()
    outImage = outImage.rotate(angle)
    outW = outImage.width
    outH = outImage.height
    displayImagePIL()

import numpy as np
def upDownImagePIL() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    outImage = inImage.copy()
    outImage = inImage.transpose(Image.FLIP_TOP_BOTTOM)
    outW = outImage.width
    outH = outImage.height
    displayImagePIL()

def sharpImagePIL() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    outImage = inImage.copy()
    outImage = outImage.filter(ImageFilter.UnsharpMask)
    outW = outImage.width
    outH = outImage.height
    displayImagePIL()

def embossImagePIL() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    outImage = inImage.copy()
    outImage = outImage.filter(ImageFilter.EMBOSS)
    outW = outImage.width
    outH = outImage.height
    displayImagePIL()

def boundaryImagePIL() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    outImage = inImage.copy()
    outImage = outImage.filter(ImageFilter.FIND_EDGES)
    outW = outImage.width
    outH = outImage.height
    displayImagePIL()

def gaussianImagePIL() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    outImage = inImage.copy()
    outImage = outImage.filter(ImageFilter.GaussianBlur)
    outW = outImage.width
    outH = outImage.height
    displayImagePIL()

def morphImagePIL() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    filename1 = askopenfilename(parent=window,filetypes=(("칼라 파일", "*.jpg;*.png;*.bmp;*.tif"), ("모든파일", "*.*")))
    if filename1 == '' or filename1 == None :
        return

    inImage1 = Image.open(filename1)
    outImage = inImage.copy()

    inImage.putalpha(1)
    inImage1.putalpha(1)

    outImage = Image.alpha_composite(inImage,inImage1)
    outW = outImage.width
    outH = outImage.height

    displayImagePIL()

import matplotlib.pyplot as plt
def histoImagePIL() :
    global window, canvas, paper, filename, inImage,outImage, inW, inH, outW, outH
    r,g,b = inImage.split()
    print(r.histogram())
    bins = list(range(256))
    plt.plot(bins, r.histogram(), 'r')
    plt.plot(bins, g.histogram(), 'g')
    plt.plot(bins, b.histogram(), 'b')

    plt.show()

#######################
#### 전역변수 선언부 ####
#######################
inImage,outImage = None,None
inW, inH, outW, outH = [0]*4
window, canvas, paper = None, None, None
filename = ""
VIEW_X, VIEW_Y = 512,512 #화면에 보일 크기 (출력용)


####################
#### 메인 코드부 ####
####################
window = Tk()
window.title('컴퓨터 비젼(칼라 라이브러리) ver 0.01')
window.geometry("500x500")

status = Label(window, text = '이미지 정보:',bd = 1 , relief = SUNKEN, anchor = W)
status.pack(side = BOTTOM,fill=X)

mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label='파일', menu=fileMenu)
fileMenu.add_command(label='파일 열기', command=openImagePIL)
fileMenu.add_separator()
fileMenu.add_command(label='파일 저장', command=saveImagePIL)

comVisionMenu1 = Menu(mainMenu)
mainMenu.add_cascade(label='화소점 처리', menu=comVisionMenu1)
comVisionMenu1.add_command(label='덧셈/뺄셈', command=addImagePIL)
# comVisionMenu1.add_command(label='파라볼라', command=paraImagePIL)
comVisionMenu1.add_command(label='모핑', command=morphImagePIL)

comVisionMenu2 = Menu(mainMenu)
mainMenu.add_cascade(label='화소영역 처리', menu=comVisionMenu2)
comVisionMenu2.add_command(label='블러링', command= blurImagePIL)
comVisionMenu2.add_command(label='샤프닝', command= sharpImagePIL)
comVisionMenu2.add_command(label='엠보싱', command= embossImagePIL)
comVisionMenu2.add_command(label='경계선 검출', command= boundaryImagePIL)
comVisionMenu2.add_command(label='가우시안 필터링', command=gaussianImagePIL)

comVisionMenu3= Menu(mainMenu)
mainMenu.add_cascade(label='기하학적 처리', menu=comVisionMenu3)
comVisionMenu3.add_command(label='확대', command= zoominImagePIL)
comVisionMenu3.add_command(label='축소', command= zoomoutImagePIL)
comVisionMenu3.add_command(label='회전', command= rotateImagePIL)
comVisionMenu3.add_command(label='상하반전', command= upDownImagePIL)

comVisionMenu4 = Menu(mainMenu)
mainMenu.add_cascade(label='통계', menu=comVisionMenu4)
comVisionMenu4.add_command(label='히스토그램', command=histoImagePIL)

window.mainloop()