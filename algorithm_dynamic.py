import sys
import time



def fibo(x):
    print('f(' + str(x) + ')', end=' ')
    if x == 1 or x == 2:
        return 1
    return fibo(x-1) + fibo(x-2)


# 탑다운 방식 = 메모이제이션 = 하향식
# 이전에 계산된 결과를 일시적으로 기록해놓는 넓은 개념을 의미
def fibo_dinamic_topDown(x):
    print('f(' + str(x) + ')', end=' ')
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo_dinamic_topDown(x-1) + fibo_dinamic_topDown(x-2)
    return d[x]



# 보텀업 방식 = 상향식
# 결과 저장용 리스트를 'DP테이블' 이라 함
def fibo_dinamic_bottomUp(x, array):
    if array[0] != 1 or array[1] != 1:
        return print("[0]과 [1]을 전처리 하십시오.")
    for i in range(3, x + 1):
        print('f(' + str(i) + ')', end=' ')
        array[i] = array[i-1] + array[i-2]    
    return array[x]
    



start = time.time()
print(fibo(7))
end = time.time()
print(end-start)

d = [0] * 1000000
start = time.time()
print(fibo_dinamic_topDown(7))
end = time.time()
print(end-start)

d = [0] * 1000
start = time.time()
d[0], d[1] = 1, 1
print(fibo_dinamic_bottomUp(999, d))
end = time.time()
print(end-start)