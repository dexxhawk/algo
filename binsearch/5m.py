n, k = map(int, input().split())

a = [0] * n
for i in range(n):
    a[i] = int(input())


l = 0
r = 10**7 + 1

for t in range (100):
    m = (l + r) * .5
    s = 0
    for i in range(n):
        s += a[i] // m
    if s >= k:
        l = m
    else:
        r = m
print(l)