from sklearn import svm
from sklearn import metrics # 정답률 확인
import pandas as pd
from sklearn.model_selection import train_test_split
import math

def changeValue(lst) :
    return [float(v)/255 for v in lst]
    # return [math.ceil(float(v)/255)for v in lst] # 소수점 올림

# 0. 훈련데이터, 테스트 데이터 준비
csv = pd.read_csv('c:/BigData/MNIST/train_10K.csv')
train_data = csv.iloc[:, 1:].values
train_data = list(map(changeValue,train_data))
train_label = csv.iloc[:,0].values
# csv = pd.read_csv('c:/BigData/MNIST/t10k_0.5K.csv')
# test_data = csv.iloc[:, 1:].values
# test_data = list(map(changeValue,test_data))
# test_label = csv.iloc[:,0].values


# 1. Classifire 생성 (선택) --> 머신러닝 알고리즘 선택
clf = svm.SVC(gamma='auto')
# clf = svm.NuSVC(gamma='auto') # 70%

# 2. 데이터로 학습 시키기
#clf.fit( [훈련 데이터],[정답] )
clf.fit(train_data, train_label) # train_data:0~1 사이 값을 받음. 예전 버전에서는 train_label 문자형 안받음

import joblib
# 학습된 모델 저장하기
joblib.dump(clf,'mnist_model_1k.dmp') # 파일을 저장하는 기능

print('저장.ok~')

# #3. 정답률을 확인 (신뢰도)
# results = clf.predict(test_data)
# score = metrics.accuracy_score(results,test_label)
# print("정답률 :", "{0:.2f}%".format(score*100))

# ## 그림 사진 보기
# import matplotlib.pyplot as plt
# import numpy as np
# img = np.array(test_data[0]).reshape(28,28)
# plt.imshow(img,cmap = 'gray')
# plt.show()

# # #4. 예측하기
# # # clf.predict( [예측할 데이터] )
# result = clf.predict([ [4.1, 3.3, 1.5, 0.2] ])
# print(result)
