n = int(input())
arr = []
for i in range(max(1, n-54), n):
    result = i
    temp = i
    while True:
        a, b = divmod(temp, 10)
        result += b
        if a == 0:
            break
        else:
            temp = a
    if result == n:
        arr.append(i)
        break
if len(arr) == 0:
    print(0)
else:
    print(min(arr))

# n = int(input())
# for i in range(max(1, n-54),n):
#     if sum(map(int,str(i)))+i == n:
#         print(i)
#         exit(0)
# print(0)
        