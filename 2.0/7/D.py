n, m = map(int, input().split())
a = list(map(int, input().split()))

segs = []
for i in range(n):
    segs.append((a[i], 0))
for i in range(m):
    l, r = map(int, input().split())
    segs.append((l, -1, i))
    segs.append((r, 1, i))

segs.sort()

cats_qty = 0
ans = [0] * m
for i in range(len(segs)):
    if segs[i][1] == -1:
        ans[segs[i][2]] = cats_qty
    elif segs[i][1] == 0:
        cats_qty += 1
    # Кол-во котят на отрезке = кол-во котят в конце - кол-во в начале
    else:
        ans[segs[i][2]] = cats_qty - ans[segs[i][2]]

print(*ans)
# O(n + m)