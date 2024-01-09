n, k = map(int, input().split())

dp = [-1] * (n + 1)
dp[0] = 0
dp[1] = 1

for i in range(2, n + 1):
    qty = 0
    for j in range(min(i, k)):
        qty += dp[i - j - 1]
    dp[i] = qty
print(dp[n])
