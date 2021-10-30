import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    x, y, dist = map(int, input().split())
    graph[x].append((dist, y))

def dijkstra(start):
    queue = []
    distance[start] = 0
    heapq.heappush(queue, (distance[start], start))
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[0]
            if cost < distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(queue, (cost, i[1]))

dijkstra(c)
print(graph)
print(distance)

cnt = 0
max_distance = 0
for d in distance:
    if d != INF:
        cnt += 1
        max_distance = max(max_distance, d)

print(cnt - 1, max_distance)
            


# 3 2 1
# 1 2 4
# 1 3 2

# 2 4