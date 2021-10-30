import sys
n, m = map(int, sys.stdin.readline().strip().split())
units = []
for _ in range(n):
    units.append(int(input()))

d = [10001] * (m + 1)

d[0] = 0
for i in range(n):
    for j in range(units[i], m+1):
        if d[j-units[i]] != 10001:
            d[j] = min(d[j], d[j-units[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])