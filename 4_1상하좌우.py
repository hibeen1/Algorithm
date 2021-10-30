import time

# 방법 1. 답지 풀이
n = int(input())
arr = input().split()

start_time = time.time()
x,y = 1,1

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

for i in arr:
    for j in range(len(move_types)):
        if i == move_types[j]:
            nx = x + dx[j]
            ny = y + dy[j]
            break
    if nx<1 or ny<1 or nx>n or ny >n:
        continue
    x,y = nx,ny
print(x,y)


end_time = time.time()
print("실행 시간 : ", end_time-start_time)



# 방법 2. 내가 푼 것
# n = int(input())
# arr = input().split()

# start_time = time.time()
# x, y = 1, 1

# for i in arr:
#     if i == 'L':
#         if y > 1:
#             y -= 1
#     elif i == 'R':
#         if y < n:
#             y += 1
#     elif i == 'U':
#         if x > 1:
#             x -= 1
#     elif i == 'D':
#         if x < n: 
#             x += 1

# print(x, y)

# end_time = time.time()
# print("실행 시간 : ", end_time-start_time)