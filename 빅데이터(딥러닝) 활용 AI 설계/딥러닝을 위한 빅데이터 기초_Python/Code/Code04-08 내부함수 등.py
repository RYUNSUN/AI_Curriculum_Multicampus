# def outFunc(v1, v2) :
#     def inFunc(n1, n2) :
#         return n1 + n2
#     return inFunc(v1, v2)
# # 내부함수는 스레드 만들 때 잘 쓰임
#
# print(outFunc(100,200))

# def hap (v1,v2) :
#     res = v1 + v2
#     return res
# hap2 = lambda v1, v2 : v1+v2 # 함수를 한 줄로 간단하게 만들어줌
#
# print(hap(100,200))
# print(hap2(100,200))

myList = [1,2,3,4,5]
# def add10(num) :
#     return num + 10
# add10 = lambda num : num+10

# for i in range(len(myList)) :
#     myList[i] = add10(myList[i])
# myList = list(map(add10, myList))
myList = list(map(lambda num : num+10, myList))

print(myList)