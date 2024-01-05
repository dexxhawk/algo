from math import pi

n = int(input())
events = []

rmin = 0
rmax = 10 ** 6 #bad practice

for i in range(1, n + 1):
    r1, r2, phi1, phi2 = map(float, input().split())
    rmin = max(rmin, r1)
    rmax = min(rmax, r2)
    events.append((phi1, -i))
    events.append((phi2, i))
events.sort()

used = set()
cntsegs = 0
for event in events:
    if event[1] < 0:
        cntsegs += 1
        used.add(-event[1])
    elif event[1] in used:
        cntsegs -= 1
ans = 0
for i in range(len(events)):
    event = events[i]
    if event[1] < 0:
        cntsegs += 1
    else:
        cntsegs -= 1
    if cntsegs == n:
        if i < len(events) - 1:
            ans += (events[i + 1][0] - events[i][0]) * (rmax ** 2 - rmin ** 2) / 2
        else:
            ans += (events[0][0] - events[len(events) - 1][0] + 2 * pi) * (rmax ** 2 - rmin ** 2) / 2
print(ans)

