N, M = map(int, input().split())

m = [0] + list(map(int, input().split()))
c = [0] + list(map(int, input().split()))
dp = [[0] * (M + 1) for _ in range(N + 1)]

ans = []

for i in range(1, N + 1):
    for j in range(0, M + 1):
        dp[i][j] = dp[i - 1][j]
        if j - m[i] >= 0:
            if dp[i - 1][j - m[i]] + c[i] > dp[i][j]:
                dp[i][j] = dp[i - 1][j - m[i]] + c[i]
                ans.append(i)


print(ans)