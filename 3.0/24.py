n = int(input())
a = [0] * n
b = [0] * n
c = [0] * n

for i in range(n):
    a[i], b[i], c[i] = map(int, input().split())

INF = 5001
dp = [INF] * (n + 1)

dp[0] = 0
dp[1] = a[0]
if n > 1:
    dp[2] = min(dp[1] + a[1], b[0])

for i in range(3, n + 1):
    dp[i] = min(dp[i - 1] + a[i - 1], dp[i - 2] + b[i - 2], dp[i - 3] + c[i - 3])

print(dp[n])


# dp[3] = min(dp[i - 1] + a[i - 1], dp[i - 2] + b[i - 2], c[i - 3])
# можно не писать, тк автоматом получается при i = 3,
# для этого dp[0] = 0, кроме i = 3 обращения к этому элементу не происходит.