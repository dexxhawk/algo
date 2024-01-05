n = int(input())
segs = [0] * 2 * n

i = 0
while i < 2 * n: 
    l, r = map(int, input().split())
    segs[i] = (l, -1)
    i += 1
    segs[i] = (r, 1)
    i += 1


segs.sort()
anslen = 0
online = 0
for i in range(len(segs)):
    if online > 0:
        anslen += segs[i][0] - segs[i - 1][0]
    if segs[i][1] == -1:
        online += 1
    else:
        online -=1
print(anslen)
    
        







