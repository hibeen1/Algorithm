# # 2 <= n <= 1000
# n = int(input())
# cost = []
# for _ in range(n):
#     cost.append(list(map(int, input().split())))

# dp = []
# dp.append([cost[0][0], cost[0][1], cost[0][2]])
# for i in range(1, n):
#     r = min(dp[i-1][1] + cost[i][0], dp[i-1][2] + cost[i][0])
#     g = min(dp[i-1][0] + cost[i][1], dp[i-1][2] + cost[i][1])
#     b = min(dp[i-1][0] + cost[i][2], dp[i-1][1] + cost[i][2])
#     dp.append([r, g, b])

# print(min(dp[n-1]))

import sys
l = sys.stdin.readlines()
d=[];m=min
for _ in l[1:]:d.append(list(map(int,_.split())))
R,G,B=0,0,0
for i in d:R,G,B=m(G,B)+i[0],m(R,B)+i[1],m(R,G)+i[2]
print(m(R,G,B))
print(l)