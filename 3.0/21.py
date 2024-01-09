n = int(input())

if n < 3:
    dp = [-1] * 3
else:
    dp = [-1] * (n + 1)

dp[0] = 1
dp[1] = 2
dp[2] = 4


for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
print(dp[n])