def cnt(x, m) -> int:
    qty = 0
    maxright = x[0] - 1
    for nowx in x:
        if nowx > maxright:
            qty += 1
            maxright = nowx + m
    return qty
# Cover our line with segments and check for every elem if they in current segment
# If not -> create the next segment
n, k = map(int, input().split())
x = list(map(int, input().split()))
x.sort()
l = -1
r = x[-1] - x[0]
while r > l + 1:
    m = (l + r) // 2
    if (cnt(x, m) <= k):
        r = m
    else:
        l = m
print(r)
