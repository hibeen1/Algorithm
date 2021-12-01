from collections
from collections import deque
n = int(input())
graph = []
for _ in range(n):
    graph.append(list(input().split()))

def bfs(graph):
    q = deque()
    for i in range(n):
        for j in range(n):
            if graph[i][j] == "T":
                q.append((i, j))
    
    while(q):
        