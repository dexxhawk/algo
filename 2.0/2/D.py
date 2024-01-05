l, k = map(int, input().split())
pos = list(map(int, input().split()))


mxm = 0
mnm = 10001

for i in range(k):
    if l % 2 != 0 and pos[i] == l // 2:
        mxm = pos[i]
        mnm = pos[i]
        break
    if pos[i] < l // 2:
        mxm = max(mxm, pos[i])
    if pos[i] >= l // 2:
        mnm = min(mnm, pos[i])

if mxm == mnm or k == 1: print(mxm)
else: print(mxm, mnm)