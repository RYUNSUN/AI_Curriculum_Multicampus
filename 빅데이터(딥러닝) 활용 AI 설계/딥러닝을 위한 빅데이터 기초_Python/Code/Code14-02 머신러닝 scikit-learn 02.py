from sklearn import svm
from sklearn import metrics # 정답률 확인


#1. Classifire 생성 (선택) --> 머신러닝 알고리즘 선택
clf = svm.SVC(gamma='auto') # svm,SVC 알고리즘 선택, svm 안에는 여러 알고리즘 존재

#2. 데이터로 학습 시키기
#clf.fit( [훈련 데이터],[정답] )
#XOR 데이터
clf.fit ( [ [0,0],
            [0,1],
            [1,0],
            [1,1]] ,
          [0,0,0,1])

#3. 정답률을 확인 (신뢰도)
results = clf.predict([[1,0],[1,1]])
score = metrics.accuracy_score(results,[0,1]) # metrics.accuracy_score([[테스트]],[테스트 결과])
print("정답률 :", score*100, '%')
print(results)

#4. 예측하기
# clf.predict( [예측할 데이터] )
# result = clf.predict([ [1,0] ])
# print(result)
