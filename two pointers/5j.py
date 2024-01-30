n, s = map(int, input().split())
a = list(map(int, input().split()))

l = 0
x = 0
ans = 0

for r in range(len(a)):
    x += a[r]
    while (x > s):
        x -= a[l]
        l += 1
    ans += r - l + 1

print(ans)