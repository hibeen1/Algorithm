n = int(input())
result = 0
if n <= 2:
    if n == 1:
        result = 1
    if n == 2:
        result = 2
else:
    a, b = 1, 2
    while (n - 2):
        result = (a + b) % 15746
        a, b = b, result
        n -= 1
print(result)

# n = int(input())
# if n > 2:
#     dp = [0] * (n+1)
#     dp[1] = 1
#     dp[2] = 2
#     for i in range(3, n+1):
#         dp[i] = dp[i-1] + dp[i-2]
# else:
#     dp = [0, 1, 2]
# print(dp[n] % 15746)


# dp[1] = 1
# dp[2] = 2
# dp[3] = 3
# dp[4] = 5
# dp[5] = 8
# dp[6] = 13
# dp[7] = 21
# dp[8] = 34