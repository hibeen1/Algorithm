import sys
from collections import deque

input = sys.stdin.readline
n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

visited = [False for _ in range(n + 1)]
result = [-1 for _ in range(n + 1)]
q = deque()
q.append(x)
result[x] = 0
visited[x] = True
while q:
    temp = q.popleft()
    for item in graph[temp]:
        if visited[item] is False:
            visited[item] = True
            q.append(item)
            result[item] = result[temp] + 1
for i in range(1, n + 1):
    if result[i] == k:
        print(i)
if k not in result:
    print(-1)
