n, m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
for i in range(n):
    x[i] = (x[i], i + 1)
for i in range(m):
    y[i] = (y[i], i + 1)

x.sort()
y.sort()

i = 0
j = 0
cnt = 0

z = [0] * n
while (i < n and j < m):
    if x[i][0] + 1 <= y[j][0]:
        z[x[i][1] - 1] = y[j][1]
        cnt += 1
        i += 1
        j += 1
    else:
        j += 1
print(cnt)
print(*z)