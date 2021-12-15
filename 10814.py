# 1 <= n <= 100000
from sys import stdin

n = int(input())

arr = []
for i in range(n):
    a, b = stdin.readline().split()
    arr.append([(int(a), i), b])

arr.sort()

for item in arr:
    print(item[0][0], item[1])

