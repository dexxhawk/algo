ans = 0
mxm = 0

while True:
    x = int(input())
    if x == 0:
        break
    if x == mxm:
        ans += 1
    if x > mxm:
        mxm = x
        ans = 1

print(ans)
    