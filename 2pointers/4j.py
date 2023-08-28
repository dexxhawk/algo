import sys

n, s = map(int, input().split())
a = list(map(int, input().split()))

l = 0
x = 0
ans = sys.maxsize

for r in range(len(a)):
    x += a[r]
    while (x >= s):
        x -= a[l]
        l += 1
    #l-1 .. r is good
    if l > 0:
        ans = min(ans, r - l + 2)

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)