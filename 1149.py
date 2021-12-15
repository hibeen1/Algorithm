# 2 <= n <= 1000
n = int(input())
cost = []
for _ in range(n):
    cost.append(list(map(int, input().split())))

def dfs(cost):
    for i in range(len(cost)):
        for j in range