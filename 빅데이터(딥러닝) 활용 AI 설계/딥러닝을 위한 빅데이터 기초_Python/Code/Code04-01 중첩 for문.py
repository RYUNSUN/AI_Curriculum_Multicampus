# i,k = 0,0
#
# for i in range(2, 10, 1) :
#     print("## %d 단 ##" % (i))
#     for k in range(1, 10, 1) :
#         print(i, '*', k, '=', i*k)

## 10 x 10 크기의 숫자를 예쁘게 출력해라 ##
import random
import random as rd #random을 rd로 줄여쓰겠다는 의미
from random import randrange,randint #randrange, randint 로 바로 쓰겠다는 의미
from random import * # 모두 random으로 쓰겠다는 의미

count = 0
for _ in range(10) :
    for _ in range(10) :
        num = randrange(0,100) # random.randint(0,99)
        # print("%2d "% (count), end='') #()를 써서 구분하기
        print("%2d " % (num), end = '')
        # count += 1
    print() # *를 10개 까지 출력하기 위해서