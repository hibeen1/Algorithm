

import time

n, m = map(int, input().split())
arr = list()
result = 0

for i in range(n):
    arr.append(list(map(int, input().split())))
    if i == 0:
        result = min(arr[i])
    else:
        result = max(result, min(arr[i]))
print(result)

