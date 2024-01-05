n, q = map(int, input().split())
a = list(map(int, input().split()))

pref = [0] * (n + 1)
for i in range(1, n + 1):
    pref[i] = a[i - 1] + pref[i - 1]


ans = [0] * q
for i in range(q):
    l, r = map(int, input().split())
    l -= 1
    ans[i] = pref[r] - pref[l]
print(*ans)
    