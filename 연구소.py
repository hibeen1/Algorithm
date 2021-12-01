import copy
from itertools import combinations

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 벽을 세울 수 있는 좌표 모두 알아내기
arr = []
for x in range(n):
    for y in range(m):
        if graph[x][y] == 0:
            arr.append((x, y))

# 그 중에 순서 상관 없이 3개 뽑는 모든 조합 알아내기
wall_3 = list(combinations(arr, 3))

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 0의 개수 알아내는 함수
def count_0(graph):
    cnt = 0
    for x in range(n):
        for y in range(m):
            if graph[x][y] == 0:
                cnt += 1
    return cnt


# 바이러스 전파 함수
# 상하좌우가 0이라면 해당 자리를 2로 만든 후 바이러스 전파
def contaminate(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (nx >= n or nx < 0 or ny >= m or ny < 0):    
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                contaminate(nx, ny)

result = 0

# 모든 조합에 대해서 반복
for i in range(len(wall_3)):
    # 매번 temp를 원래 그래프로 초기화
    temp = copy.deepcopy(graph)

    # 해당 조합으로 일시적인 맵 설정
    for x, y in wall_3[i]:
        temp[x][y] = 1

    # 바이러스 전파
    for x in range(n):
        for y in range(m):
            # 해당 자리에 바이러스가 있을 경우 전염 함수 작동
            if temp[x][y] == 2:
                contaminate(x,y)
    
    # 바이러스 전파된 맵에 대하여 0의 개수 count
    # 0의 개수가 신고가를 찍으면 result 갱신
    result = max(result, count_0(temp))

print(result)



    





