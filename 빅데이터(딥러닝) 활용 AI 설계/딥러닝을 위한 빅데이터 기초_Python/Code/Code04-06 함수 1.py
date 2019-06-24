# 두 수를 받아서 더한 값을 반환하는 함수
# def plus(v1, v2) : # v1,v2 :parameter
#     result = 0
#     result = v1 + v2
#     return result

def calc(v1, v2, v3 = 0) : # v1,v2 :parameter
    result1 = v1 + v2 + v3
    result2 = v1 - v2 - v3
    return result1, result2

def calc2(*para) : #넘겨주는 parameter 모두 계산하기
    res = 0
    for num in para :
        res += num
    return res

## 메인 코드부
hap1,hap2 = calc(100, 200, 300)
hap = calc2(12,3,3,4,5,6,7)
print(hap)

