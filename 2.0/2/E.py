n = int(input())
folder = list(map(int, input().split()))

ans = 0
mxm = 0
qty = 0
for i in range(len(folder)):
    if folder[i] > mxm:
        mxm = folder[i]
ans = qty - mxm
print(ans)

