# 각 노드가 연결된 정보를 표현(2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 표현(1차원 리스트)
visited = [False] * 9

def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end = ' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, 1, visited)


# <문제 1> 음료수 얼려 먹기
# 첫 번 째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어진다. (1 <= N,M <= 1000)
# 두 번 째 줄부터 N+1 번 째 줄까지 얼음 틀의 형태가 주어진다
# 이 때 구멍이 뚫려있는 부분은 0, 아닌 부분은 1
# 나눌 수 있는 아이스크림의 형태 개수 출력
# 입력 예시 :
#         4 5
#         00110
#         00011
#         11111
#         00000
# 출력 예시:
#         3

# # 문제 풀이

# def dfs(x, y):
#     # 주어진 범위를 벗어나는 경우에는 즉시 종료
#     if x<= -1 or x >= n or y <= -1 or y >= m:
#         return False
#     # 현재 노드를 아직 방문하지 않았다면
#     if graph[x][y] == 0:
#         # 해당 노드 방문 처리
#         graph[x][y] = 1
#         # 상하좌우의 위치들도 모두 재귀적으로 호출
#         dfs(x-1, y)
#         dfs(x, y-1)
#         dfs(x+1, y)
#         dfs(x, y+1)
#         return True
#     return False

# # N, M을 공백을 기준으로 구분하여 입력 받기
# n, m = map(int, input().split())

# # 2차원 리스트의 맵 정보 입력 받기
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))

# # 모든 노드에 대하여 음료수 채우기
# result = 0
# for i in range(n):
#     for j in range(m):
#         # 현재 위치에서 DFS 수행
#         if dfs(i, j) == True:
#             result += 1
# print(result)



