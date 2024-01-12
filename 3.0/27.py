n, m = map(int, input().split())

a = [[] for _ in range(n)]

# BASE:
for i in range(n):
    a[i] = list(map(int, input().split()))

dp = [[0] * m for _ in range(n)]
dp[0][0] = a[0][0]
prev = [[0] * m for _ in range(n)]

for i in range(1, n):
    dp[i][0] = dp[i - 1][0] + a[i][0]
    prev[i][0] = (i - 1, 0, "D")
for i in range(1, m):
    dp[0][i] = dp[0][i - 1] + a[0][i]
    prev[0][i] = (0, i - 1, "R")


# SOLVE:
for i in range(1, n):
    for j in range(1, m):
        if dp[i - 1][j] > dp[i][j - 1]:
            dp[i][j] = dp[i - 1][j] + a[i][j]
            prev[i][j] = (i - 1, j, "D")
        else:
            dp[i][j] = dp[i][j - 1] + a[i][j]
            prev[i][j] = (i, j - 1, "R")
print(dp[n - 1][m - 1])



path = [""] * (n + m - 2)
prev_elem = prev[n - 1][m - 1]
for i in range(n + m - 2):
    path[i] = prev_elem[2]
    prev_elem = prev[prev_elem[0]][prev_elem[1]]

print(*(path[::-1]))
    





