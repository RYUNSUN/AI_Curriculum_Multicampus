#p. 358
import os
for dirName,subDirLsit,fnames in os.walk('c:/images/') :
    for fname in fnames :
        # print(fname)
        # ff = os.path.splitext(fname)
        # print(os.path.split(fname)[1])
        if os.path.splitext(fname)[1].upper() == '.GIF' : # 파일 이름과 확장명을 나눠줌, [1]은 확장명을 출력하라는 의미
            print(os.path.join(dirName,fname))