n, m = map(int, input().split())
arr = list(map(int, input().split()))
result = int(1e9)
for i in range(0, n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if arr[i] + arr[j] + arr[k] == m:
                result = m
                break
            else:
                if arr[i] + arr[j] + arr[k] < m:
                    if abs(result - m) > abs(m - arr[i] - arr[j] - arr[k]):
                        result = arr[i] + arr[j] + arr[k]
print(result)