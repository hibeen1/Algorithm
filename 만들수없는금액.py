import itertools
from coding import random_List
# n = int(input())
# arr = list(map(int, input().split()))

# # 나의 풀이
# n = 1000
# print("here")
# arr = random_List(n, 1, 1000000)
# print("here2")

# arr2 = list()
# print("here3")
# for i in range(1, n+1):
#     arr2 += list(itertools.combinations(arr, i))
# arr3 = set()
# print("here4")
# # print(arr2)
# for i in range(len(arr2)):
#     arr3.add(sum(arr2[i]))
# arr3 = sorted(list(arr3))
# # print(arr3)
# for i in range(1, len(arr3)):
#     if arr3[i] - arr3[i-1] != 1:
#         print(arr3[i-1] + 1)
#         break
#     if i == len(arr3) - 1:
#         print(arr3[i] + 1)


# 책 풀이
# n = int(input())
# data = list(map(int, input().split()))
n = 1000

data = random_List(n, 1, 10)
data.sort()
print(data)

target = 1
for x in data:
    if target < x:
        break
    target += x

print(target)


