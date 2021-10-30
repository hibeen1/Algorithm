import time

n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)


# 방법 1
start_time = time.time()
result = 0
cnt = 0
if arr[0] == arr[1]:
    print(arr[0]*m)

while(True):
    if cnt == m:
        break
    for _ in range(k):
        cnt += 1
        result += arr[0]
    cnt += 1
    result += arr[1]

print(result)
end_time = time.time()
print("실행 시간 : ", end_time-start_time)


# 방법 2
start_time = time.time()
result = 0
cnt2 = m//(k+1)
result += cnt2*((arr[0]*k)+arr[1])
result += (m%(k+1))*arr[0]

print(result)
end_time = time.time()
print("실행 시간 : ", end_time-start_time)



