# from collections import deque

# n = int(input())
# k = int(input())
# location_of_apples = []
# for i in range(k):
#     location_of_apples.append(list(map(int, input().split())))
#     location_of_apples[i][0] -= 1
#     location_of_apples[i][1] -= 1
    

# l = int(input())
# changes = [[0, 0] for _ in range(l)]
# for i in range(l):
#     a, b = input().split()
#     changes[i][0] = int(a)
#     changes[i][1] = b

# # 우하좌상
# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]

# # 방향 오른쪽으로 초기화
# direction = 0

# def turn_left(direction):
#     if direction == 0:
#         direction = 4
#     return direction - 1

# def turn_right(direction):
#     if direction == 3:
#         direction = - 1
#     return direction + 1


# time = 0
# head = [0, 0]
# tail = [0, 0]
# body = deque()
# body.append(head)


# while True:
#     # 시간 추가
#     time += 1

#     # 첫 방향 전환 시점이 n보다 같거나 클 때
#     if changes[0][0] >= n:
#         time = n
#         break

#     # 머리 이동
#     new_head = [0, 0]
#     new_head[0] = head[0] + dx[direction]
#     new_head[1] = head[1] + dy[direction]


#     # 벽을 마주했을 경우
#     if new_head[0] == -1 or new_head[0] == n or new_head[1] == -1 or new_head[1] == n:
#         if time <= changes[0][0]:
#             pass
#         else:
#             break

#     # 자기 몸통을 마주했을 경우
#     if new_head in body:
#         break
    
#     # head 업데이트 후 body에 추가
#     head = new_head
#     body.append(head)

#     # 사과가 있을 경우
#     if head in location_of_apples:
#         del location_of_apples[location_of_apples.index(head)]
#         pass
#     else:
#         body.popleft()
#         tail = body[0]
    
#     # 방향이 바뀔 경우
#     for i in range(l):
#         if time == changes[i][0]:
#             if changes[i][1] == 'L':
#                 direction = turn_left(direction)
#             elif changes[i][1] == 'D':
#                 direction = turn_right(direction)
    
#     # print(time, "head:", head, "tail:", tail, "body:", body)
# print(time)
      

# # 6
# # 3
# # 3 4
# # 2 5
# # 5 3
# # 3
# # 3 D
# # 15 L
# # 17 D

# # 9

# # 10
# # 4
# # 1 2
# # 1 3
# # 1 4
# # 1 5
# # 4
# # 8 D
# # 10 D
# # 11 D
# # 13 L

# # 21

# 10
# 5
# 1 5
# 1 3
# 1 2
# 1 6
# 1 7
# 4
# 8 D
# 10 D
# 11 D
# 13 L

# 13
        

n = int(input())
k = int(input())
data = [[0] * (n + 1) for _ in range(n + 1)]
info = []

for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulator():
    x, y = 1, 1
    data[x][y] = 2
    direction = 0
    time = 0
    index = 0
    q = [(x, y)]
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))
        else:
            time += 1
            break
        x, y = nx, ny
        time += 1
        if index < l and time == info[index][0]:
            direction = turn(direction, info[index][1])
            index += 1
    return time

print(simulator())

