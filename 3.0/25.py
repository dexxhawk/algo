n = int(input())
a = list(map(int, input().split()))

if n < 2:
    print(0)
elif n == 2:
    print(a[1] - a[0])
else:
    a.sort()
    INF = 10**4 + 1
    dp = [INF] * (n + 1)
    dp[2] = a[1] - a[0]
    dp[3] = a[2] - a[0]

    for i in range(4, n + 1):
        dp[i] = min(dp[i - 1], dp[i - 2]) + a[i - 1] - a[i - 2]
    
    print(dp[n])
