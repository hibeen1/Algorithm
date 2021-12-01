
# # 입력
# n, k = map(int, input().split())
# graph = []
# for _ in range(n):
#     graph.append(list(map(int, input().split())))
# s, x, y = map(int, input().split())


# # 첫 번째 방법. 단순 생각
# # 백준 랭커의 위엄이다 이게!

# def distance(nx, ny):
#     return abs(nx-x+1) + abs(ny-y+1)
# result = dict()
# for i in range(k):
#     result[i+1] = 2*n
# for i in range(n):
#     for j in range(n):
#         if graph[i][j] != 0:
#             result[graph[i][j]] = min(result[graph[i][j]], distance(i, j))
# print(result)
# for key in result.keys():
#     result[key] -= s
# print(result)

# # value들이 전부 +면(s가 너무 작아 바이러스가 안 퍼졌다면) 0 출력, 아니면 value 기준으로 sort한 것 중 제일 앞에 거 출력
# is_safe = True
# for value in result.values():
#     if value <= 0:
#         is_safe = False
#         break

# if is_safe == True:
#     print(0)
# else:
#     result = sorted(result.items(), key=lambda x: x[1])
#     print(result[0][0])
    

    


# # 두 번쨰 방법. 맵을 계속 업데이트 하기

# # 상하좌우
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def append_candidates(x, y):
#     temp = []
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if not(nx > n-1 or nx < 0 or ny > n-1 or ny < 0):
#             if graph[nx][ny] != 0:
#                 temp.append(graph[nx][ny])
#     return temp




# def sumMatrix(A,B):
#     for i in range(len(A)) :
#         for j in range(len(A[0])):
#             A[i][j] += B[i][j] 
#     return A

# # is_all_contaminated = False
# def update(graph):
#     graph_0 = [[0] * n for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if graph[i][j] == 0:
#                 temp = append_candidates(i, j)
#                 if len(temp) == 0:
#                     continue
#                 else:
#                     graph_0[i][j] = min(temp)
#                 del(temp)
#     sumMatrix(graph, graph_0)
#     del(graph_0)
    

# # 맵을 업데이트 한다...
# while s > 0:
#     update(graph)
#     s -= 1

# print(graph[x-1][y-1])


from collections import deque
 
N, K = map(int, input().split())
graph = []
virus = []
for i in range(N):
  graph.append(list(map(int, input().split())))
  for j in range(N):
    if graph[i][j] != 0:
      virus.append(((graph[i][j], i, j)))
S, X, Y = map(int, input().split())
 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
 
def bfs(s, X, Y):
  q = deque(virus)
  count = 0
  while q:
    if count == s:
      break
    for _ in range(len(q)):
      prev, x, y = q.popleft()
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
          if graph[nx][ny] == 0:
            graph[nx][ny] = graph[x][y]
            q.append((graph[nx][ny], nx, ny))
    count += 1
    # for i in range(N):
    #     print(graph[i])
    # print()
  return graph[X-1][Y-1]
 
virus.sort()
print(bfs(S, X, Y))