n = int(input())

arr = []
for _ in range(n):
    temp = input().split()
    arr.append((temp[0], int(temp[1])))

arr.sort(key=lambda name: name[1])

for name in arr:
    print(name[0], end=" ")
