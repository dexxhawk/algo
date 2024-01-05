#PAY ATTENTION TO THE KEY OF THE SORT
#CAN BE EASIER LIKE IN GUIDE
s = int(input())
a = input().split()
b = input().split()
c = input().split()

a = list(map(int, a[1:]))
b = b[1::]
for i in range(len(b)):
    b[i] = (int(b[i]), i)
b.sort(key=lambda x: (x[0], -x[1]))
c = c[1::]
for i in range(len(c)):
    c[i] = (int(c[i]), i)
c.sort(key=lambda x: (-x[0], x[1]))
flag_i = 0
for i in range(len(a)):
    if flag_i: break
    k = 0
    for j in range(len(b)):
        while (k < len(c) - 1 and a[i] + b[j][0] + c[k][0] > s):
            k += 1
        if a[i] + b[j][0] + c[k][0] == s and (not flag_i or (i, b[j][1], c[k][1]) < ans):
            ans = (i, b[j][1], c[k][1])
            flag_i = 1
if not flag_i:
    print(-1)
else:
    print(*ans)