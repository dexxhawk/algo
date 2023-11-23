n = int(input())

dp0 = 1
ans = dp1 = 2

for i in range(2, n + 1):
    ans = dp0 + dp1
    dp0 = dp1
    dp1 = ans
print(ans)
