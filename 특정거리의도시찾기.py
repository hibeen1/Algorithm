from collections import deque
import sys

n, m, k, x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

distance = [-1 for _ in range(n + 1)]
distance[x] = 0

q = deque()
q.append(x)
while q:
    temp = q.popleft()
    for i in graph[temp]:
        if distance[i] == -1:
            distance[i] = distance[temp] + 1
            q.append(i)
print(distance)
if k not in distance:
    print(-1)
else:
    for i in range(len(distance)):
        if distance[i] == k:
            print(i)


