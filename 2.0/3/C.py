seq = list(map(int, input().split()))
dct = dict()

for elem in seq:
    if elem not in dct:
        dct[elem] = 1
    else:
        dct[elem] += 1

for key, value in dct.items():
    if value == 1:
        print(key, end=' ')