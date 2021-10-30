from coding import random_String
# 나의 풀이
# arr = list(map(int, input()))
string = random_String(20, 0, 9)
arr = list(map(int, string))
result = 0

for i in arr:
    if result * i >= result + i:
        result *= i
    else:
        result += i

print(result)  


# # 책 풀이
# # data = input()
data = string

result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num
print(result)


# 02984
# 576

# 567
# 210

# 1212
# 8

