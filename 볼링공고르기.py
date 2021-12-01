from coding import random_List
import time

# # 나의 풀이
# # n, m = map(int, input().split())
# # data = list(map(int, input().split()))

n = 10000000
m = 10
data = random_List(n, 1, m)

start = time.time()
dic = dict()
for i in range(1, m+1):
    dic[i] = 0
for i in range(n):
    dic[data[i]] += 1
result = 0
for i in range(1, m+1):
    temp = 0
    for j in range(i+1, m+1):
        temp += dic[j]
    result += dic[i] * temp
print(result)
end = time.time()
print("나의 풀이 :", end - start)

# 5 3
# 1 3 2 3 2
# 8

# 8 5
# 1 5 4 3 2 4 5 2
# 25

# n, m = map(int, input().split())
# data = list(map(int, input().split()))

start = time.time()
array = [0] * 11
for x in data:
    array[x] += 1

result = 0
for i in range(1, m+1):
    n -= array[i]
    result += array[i] * n

print(result)
end = time.time()
print("책 풀이 :", end - start)