n, m = map(int, input().split())

dp = [[0] * m for _ in range(n)]

#BASE:
dp[0][0] = 1
if n >=3 and m >= 2:
    dp[2][1] = 1
if n >= 2  and m >= 3:
    dp[1][2] = 1


for i in range(2, n):
    for j in range(2, m):
        dp[i][j] = dp[i - 2][j - 1] + dp[i - 1][j - 2]

print(dp[n - 1][m - 1])


