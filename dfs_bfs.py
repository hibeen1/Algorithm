from collections import deque
import time

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end='')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end='')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 인접 리스트 형태의 그래프
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
visited = [False] * 9

a = time.time()
dfs(graph, 1, visited)
b = time.time()
print("\ndfs time : ", b-a)

visited = [False] * 9
a = time.time()
bfs(graph, 1, visited)
b = time.time()
print("\nbfs time : ", b-a)