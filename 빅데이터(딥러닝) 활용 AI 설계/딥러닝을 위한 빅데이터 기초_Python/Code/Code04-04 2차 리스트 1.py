# 3 x 4 크기의 리스트 조작하기
#{1) 2차원 빈 리스트 생성
image = [[0 , 0 , 0 , 0], # 한 행
         [0 , 0 , 0 , 0],
         [0 , 0 , 0 , 0]  ]

# (2) 대입 --> 파일에서 로딩...
# 파일이 없으므로 일단 랜덤하게 데이터 입력
import random
for i in range(0,3) : # 3행
    for k in range(0,4) : #4열
        image[i][k] = random.randint(0,255)

# (3) 데이터 처리/변환/분석.... --> 영상 밝게 하기 (100)
for i in range(0,3) : # 3행
    for k in range(0,4) : #4열
        image[i][k] += 100

# (4) 데이터 출력
for i in range(0,3) : # 3행
    for k in range(0,4) : #4열
        if image[i][k] > 255:
            image[i][k] = 255
        print("%3d " % (image[i][k]), end='')

    print()