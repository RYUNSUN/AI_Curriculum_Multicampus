# 배열 : 모든 원소가 같은 자료형, 원소의 개수 변경 X
# ndarray 지원 => 선형대수 계산
#벡터화 연산
import numpy as np
arr=np.array([1,2,3]) # 리스트를 배열로 변환해서 출력
print(type(arr)) # n차원 배열로 출력, numpy 기본 자료형
ans = []

for i in arr : # arr 배열에 저장되어있는 요소 하나씩 추출해서 i 변수에 담아라
    ans.append(2*i) # 리스트에 요소 추가
print(ans) # 리스트 요소 하나씩 불러와 3번 수행한 결과

print(2*arr) # 벡터화 연산, 한번만 수행한 결과

li = [1,2,3]
print(li*2) # 리스트의 길이가 2배가 됨 [1, 2, 3, 1, 2, 3]

a = np.array([1,2])
b = np.array([10,20])
print(3*a+b) # [13 26]

arr=np.array([1,2,3])
print(arr==2) # 벡터 연산
print((arr<2) & (arr>0))

c=np.array([[1,2,3],[4,5,6]]) # 2*3 array
print(len(c)) # 행의 개수
print(len(c[0])) # 열의 개수

# 배열의 차원(ndim, shape_
a = np.array([1,2,3])
print(a.ndim)
print(a.shape)

a2 = np.array([[1,2,3],[4,5,6]])
print(a2.ndim)
print(a2.shape)

a3 = np.array([1,2,3,4,5])
print("a3 :", a3[-1])

a4 = np.array([[1,2,3],[4,5,6]]) # 2,3
print(a4.ndim)
print(a4.shape)
print(a4[0]) # [1 2 3]
print(a4[0][1]) # a4 참조하여 2 출력
print(a4[0,1]) # 어떤 특정 요소 직접 지정

# 5 참조
print(a4[1])
print(a4[-1,1]) # 5 출력
print(a4[-1,-1]) # 6 출력
print(a4[-1,-2]) # 5 출력

# 5,6 슬라이싱
print(a4[1,1:3])
print(a4[1,1:]) # 1:3 = 1: (1번부터 끝까지 출력)

# f(x)=w1x1 + w2x2 + ... + wnxn + b : w(가중치), x(변수)
a = np.zeros((5,2),dtype="i") # 요소 전부 다 0으로 값을 줌. 초기화할 떄 많이 쓰임. dype="i"(정수형)
print(a) # type의 default는 실수형

b = np.empty((5,2)) # 초기화하지 않으면 쓰레기값이 들어감
print(b)

# arange 특정한 규칙에 따라 수열을 만들때 사용
print(np.arange(10))

print(np.arange(10,50,3)) # 10부터 49까지 3씩 증가

print(np.linspace(0,100,5)) # 선형공간(구간)을 만들 때 사용. 0~100까지 5개의 구간으로 생성됨 [  0.  25.  50.  75. 100.]
print(np.logspace(0.1,1,10)) # 로그공간(구간)

# 전치행렬 : 행과 열을 바꾼 행렬
# f(x) = wx+b
print(a)
print(a.T)
b=np.arange(12)
print(b)
c=b.reshape(4,3) # 1차원 -> 2차원, 4행 3열로 변환
d=b.reshape(4,-1)
print(c)
print(d)

# 1차원 -> 다차원 : reshape
# 다차원 -> 1차원 : ravel, flatten
print(c.flatten())
print(c.ravel())

x=np.arange(5)
print(x)
x=x.reshape(1,5)
print(x)
x=x.reshape(5,1)
print(x)

print(x[:,np.newaxis]) # 차원 1 증가시킬 때 사용하는 옵션

## stack 함수
a1 = np.ones((2,3)) # 모든 원소를 1로 만들어줌
print(a1)
a2 = np.zeros((2,3)) # 모든 원소를 0으로 만들어줌
print(a2)
print(np.hstack([a1,a2])) # 행의 수가 같은 2개 이상의 배열을 좌우로 연결
print(np.vstack([a1,a2])) # 열의 개수가 같은 2개 이상의 배열을 위아래로 연결
