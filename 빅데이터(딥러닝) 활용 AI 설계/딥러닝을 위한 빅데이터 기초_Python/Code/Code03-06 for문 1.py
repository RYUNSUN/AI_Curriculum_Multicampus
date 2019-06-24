### 1부터 100까지의 합계

hap = 0

for i in range(0,101,1) : # range(0,101), range(101)
    hap += i

print(hap)

"""
퀴즈 4-1. 1부터 100까지 홀수의 합계
퀴즈 4-2. 1부터 100까지 7의 배수의 합계
퀴즈 4-3. 12345부터 100000까지 7878의 배수의 합계 
"""

### 퀴즈 4-1. 1부터 100까지 홀수의 합계
hap = 0

for i in range(1,101,2) : # range(0,101), range(101)
        hap += i

print(hap)

### 퀴즈 4-2. 1부터 100까지 7의 배수의 합계
hap = 0

for i in range(7,101,7) : # range(0,101), range(101)
        hap += i

print(hap)

### 퀴즈 4-3. 12345부터 100000까지 7878의 배수의 합계
hap = 0

for i in range(12345,100001,1) : # range(0,101), range(101)
        if i % 7878 == 0 :
            hap += i

print(hap)