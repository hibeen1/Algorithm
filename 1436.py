n = int(input())
temp = 666
cnt = 0
# arr = []
while True:
    if cnt == n:
        break
    if '666' in str(temp):
        print(temp)
        # arr.append(temp)
        cnt += 1
    temp += 1
# print(arr[n-1])
print(temp-1)
