n, m = map(int, input().split())
INF = 40 * 100 + 1
a = [[]for _ in range(n + 1)]

a[0] = [INF] * m 
for i in range(1, n + 1):
    a[i] = [INF] + list(map(int, input().split()))


dp = [[INF] * (m + 1) for _ in range(n + 1)]
dp[1][0] = dp[0][1] = 0 #BASE

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + a[i][j]

print(dp[i][j])




