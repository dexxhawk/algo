n = int(input())

dct = {}
for i in range(n):
    a, d = map(int, input().split())
    if a not in dct:
        dct[a] = 0
    dct[a] += d

for key in sorted(dct):
    print(key, dct[key]) 

