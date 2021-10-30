from coding import random_String
import time
import math

data = random_String(1000000, 0, 1)
start = time.time()
count0 = 0
count1 = 0

if data[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        if data[i + 1] == '1':
            count0 += 1
        else:
            count1 += 1
print(min(count0, count1))
end = time.time()
print("책 풀이 :", end - start)

# # 나의 풀이

# s = input()
s = data

start = time.time()
cnt = 0
for i in range(1, len(s)):
    if s[i] != s[i-1]:
        cnt += 1

print(math.ceil(cnt/2))
end = time.time()
print("나의 풀이 :", end - start)


# # 1 -> 1
# # 2 -> 1
# # 3 -> 2
# # 4 -> 2
# # 5 -> 3
# # 6 -> 3



