import random

numbers = []

for _ in range(0,10) : # for (i=0; i<=10; i++)
    numbers.append(random.randint(0,9))

print(numbers)

## num 써먹기
for num in range(0,10) :
    if num not in numbers :
        print(num, '없어요')