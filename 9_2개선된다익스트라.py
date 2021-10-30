# 힙 자료구조를 이용, O(ElogV)를 보장한다.
# 힙 이란 우선순위 큐를 구현하기 위하여 사용하는 자료구조 중 하나.
# 우선순위 큐란 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 큐

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INF", end=" ")
    else:
        print(distance[i], end=" ")


# INF = sys.maxsize
# input = sys.stdin.readline
# n, e = map(int, input().split())
# graph = [[] for i in range(n+1)]
# distance = [INF] * (n+1)
# for _ in range(e):
# 	a, b, c = map(int, input().split())
# 	graph[a].append((c, b))
# 	graph[b].append((c, a))
# start = int(input())

# def dijkstra(start):
# 	queue = []
# 	distance[start] = 0
# 	heapq.heappush(queue, (distance[start], start))
# 	cnt = 0
# 	while queue:
# 		dist, now = heapq.heappop(queue)
# 		print(dist, now, distance[now])
# 		if distance[now] < dist:
# 			continue
# 		for i in graph[now]:
# 			cost = dist + i[0]
# 			if cost < distance[i[1]]:
# 				distance[i[1]] = cost
# 				heapq.heappush(queue, (cost, i[1]))
# dijkstra(start)
# for i in range(1, n+1):
# 	print(i, end="")
# 	print(":", distance[i])



# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2
