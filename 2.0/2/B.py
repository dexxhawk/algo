a = list(map(int, input().split()))

ans = 0
d = [0] * len(a) 

cur_d = 0
flag = 1
for i in range(len(a)):
    if a[i] != 2 and flag: continue
    if a[i] == 1:
        d[i] = cur_d 
    elif a[i] == 2:
        flag = 0
        cur_d = 0
    cur_d += 1

cur_d = 0
flag = 1
for i in range(len(a) - 1, -1, -1):
    if a[i] != 2 and flag: continue
    if a[i] == 1 and cur_d != 0 and (d[i] > cur_d or d[i] == 0):
        d[i] = cur_d
    elif a[i] == 2:
        flag = 0
        cur_d = 0
    cur_d += 1
print(max(d))