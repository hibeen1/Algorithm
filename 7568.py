n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

# 정확히 n^2 시간복잡도 

for i in range(n):
    cnt = 1
    for j in range(n):
        if j != i:
            if arr[j][0] > arr[i][0] and arr[j][1] > arr[i][1]:
                cnt += 1
    arr[i].append(cnt)

for i in arr:
    print(i[2], end = ' ')

