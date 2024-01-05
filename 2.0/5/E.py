s = int(input())
a = input().split()
b = input().split()
c = input().split()

a = list(map(int, a[1:]))
b = list(map(int, b[1:]))
c = list(map(int, c[1:]))
dct ={}

for i in range(len(c)):
    if c[i] not in dct:
        dct[c[i]] = i

flag = 0
for i in range(len(a)):
    if flag:
        break
    for j in range(len(b)):
        if s - a[i] - b[j] in dct:
            flag = 1
            print(i, j, dct[s - a[i] - b[j]])
            break

if not flag:
    print(-1)