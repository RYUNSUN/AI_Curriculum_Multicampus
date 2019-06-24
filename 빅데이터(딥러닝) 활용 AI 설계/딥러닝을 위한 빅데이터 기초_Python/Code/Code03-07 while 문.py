
hap = 0

#for i in range(0,101,1) :
#   hap += i
# i = 0
# while i < 101 :
#     hap += i
#     i += 1

#몇 번 돌려야할지 모를 때는 무한루프를 써야함
i = 0
while True :
    hap += i
    if hap > 10000 :
        break
    i += 1

print(hap)