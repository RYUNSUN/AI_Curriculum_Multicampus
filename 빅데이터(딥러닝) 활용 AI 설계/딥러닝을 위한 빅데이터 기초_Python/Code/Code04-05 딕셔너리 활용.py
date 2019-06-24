import operator

ttL = [ ('토마스',5), ('헨리', 8), ('에드워드',9), ('토마스',12),
        ('에드워드',1) ]

tD = {}
tL = {}
tR, cR = 1, 1 #totalRank 는 같으면 등 수 바뀌지 않음

for tmpTup in ttL : # 하나씩 꺼내서 수행
    tName = tmpTup[0]
    tWeight = tmpTup[1]
    print(tName)
    print(tWeight)
    if tName in tD :
        tD[tName] += tWeight
    else :
        tD[tName] = tWeight

# print(tD)
print(list(tD.items())) # 튜플로 묶어 리스트로 출력
tL = sorted(tD.items(), key = operator.itemgetter(1), reverse=True) # operator.itemgetter(키의 위치)
print(tL)

print("기차   \t총 수송량   \t순위")
print('------------------------------')
print(tL[0][0],'\t',tL[0][1],'\t',cR)
for i in range(1,len(tL)) :
    if tL[i][1] == tL[i-1][1] :
        pass
    else :
        cR = tR
    print(tL[i][0], '\t', tL[i][1], '\t', cR)