def findroot(a):
    l = -(10**18)
    r = 10**18
    for _ in range(115):
        m = (l + r) / 2
        if ((a * m ** 3 + b * m ** 2 + c * m + d >= 0) == (a > 0)):
            r = m
        else:
            l = m
    return l
a, b, c, d = map(int, input().split())
# Only 1 root => (x - l)^3 
# Sign depends on a
ans = findroot(a)
print(ans)
