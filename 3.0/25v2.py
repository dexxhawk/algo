n = int(input())
a = list(map(int, input().split()))

if n < 2:
    print(0)
elif n == 2:
    print(a[1] - a[0])
else:
    a.sort()

    dp2 = a[1] - a[0]
    dp3 = a[2] - a[0]
    ans = dp3

    for i in range(3, n):
        ans = a[i] - a[i - 1] + min(dp3, dp2)
        dp2 = dp3
        dp3 = ans
    print(ans)