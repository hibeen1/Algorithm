import time

n, k = map(int, input().split())
temp = n

# 방법 1. 단순 그리디 접근
start_time = time.time()
cnt = 0

while(True):
    if n== 1:
        break
    else:
        cnt += 1
    if n%k == 0:
        n = n//k
    else:
        n -= 1

print(cnt)


end_time = time.time()
print("실행 시간 : ", end_time-start_time)




#방법 2. 효율적인 접근
start_time = time.time()
cnt = 0

while(True):
    target = (temp//k) * k
    cnt += (temp - target)
    temp = target

    if temp < k:
        break
    
    cnt += 1
    temp //= k

cnt += (temp-1)
print(cnt)


end_time = time.time()
print("실행 시간 : ", end_time-start_time)


