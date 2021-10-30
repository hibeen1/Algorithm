from collections import deque

# graph = [
#     [],
#     [2, 3, 8],
#     [1, 7],
#     [1, 4, 5],
#     [3, 5],
#     [3, 4],
#     [7],
#     [2, 6, 8],
#     [1, 7]
# ]

# visited = [False] * 9

# def bfs(graph, start, visited):
#     # 큐 구현을 위해 deque 라이브러리 사용
#     queue = deque([start])
#     # 현재 노드를 방문 처리
#     visited[start] = True
#     # 큐가 빌 때까지 반복
#     while queue:
#         # 큐에서 하나의 원소를 뽑아 출력하기
#         v = queue.popleft()
#         print(v, end = ' ')
#         # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True

# bfs(graph, 1, visited)




# <문제 2> 미로 탈출
# N x M 의 직사각형 형태의 미로. 괴물이 있음!
# 현재 위치는 (1,1), 출구는 (N,M). 한 번에 한 칸 씩.
# 괴물이 있는 곳은 0, 없는 곳은 1.
# 탈출하기 위해서 움직여야 하는 최소 칸의 개수는?
# (칸을 셀 때는 시작 칸과 마지막 칸도 포함해서 계산)
# 첫 째 줄에 두 정수 N, M 주어짐. (4 <= N,M <= 200)
# 다음 부터는 미로 정보 주어짐

# 입력 예시 :
#         5 6
#         101010
#         111111
#         000001
#         111111
#         111111
# 출력 예시 :
#         10

# 문제 풀이

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    # 큐가 빌 때까지 반복하기
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른 쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 가지 방향 정의(좌, 우, 하, 상)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS를 수행한 결과 출력
print(bfs(0,0))


