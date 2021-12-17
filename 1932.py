n = int(input())
triangle = []
for _ in range(n):
    triangle.append(list(map(int, input().split())))
dp = [triangle[0]]

for i in range(1, n):
    print(i)
    print(dp)
    print(triangle[i][0])
    temp = [dp[i-1][0] + triangle[i][0]]
    for j in range(i-1):
        # print(dp[i-1][j], triangle[i][j+1], dp[i-1][j+1])
        temp.append(max(dp[i-1][j] + triangle[i][j+1], dp[i-1][j+1] + triangle[i][j+1]))
    temp.append(dp[i-1][i-1] + triangle[i][i])
    dp.append(temp)
    print(dp)
    # temp.clear()

print(max(dp[n-1]))

# dp[0] = triangle[0][0]

# dp[1][0] = triangle[0][0] + triangle[1][0]
# dp[1][1] = triangle[0][0] + triangle[1][1]

# dp[2][0] = dp[1][0] + triangle[2][0]
# dp[2][1] = max((dp[1][0] + triangle[2][1]), (dp[1][1] + triangle[2][1]))
# dp[2][2] = dp[1][1] + triangle[2][2]

# dp[3][0] = dp[2][0] + triangle[3][0]
# dp[3][1] = max((dp[2][0] + triangle[3][1]), (dp[2][1] + triangle[3][1]))
# dp[3][2] = max((dp[2][1] + triangle[3][2]), (dp[2][2] + triangle[3][2]))
# dp[3][3] = dp[2][2] + triangle[3][3]

# dp[i]
