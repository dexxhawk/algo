a, k, b, m, x = map(int, input().split())

l = 0
r = x * 2 // a + 1 

while r > l + 1:
    mid = (l + r) // 2
    if (a * (mid - mid // k) + b * (mid - mid // m) >= x):
        r = mid
    else:
        l = mid
print(r)