n = int(input())
cargos = [0] * 2 * n

i = 0
while i < 2 * n:
    t, l = map(int, input().split())
    cargos[i] = (t, -1)
    i += 1
    cargos[i] = (t + l, 1)
    i += 1

cargos.sort(key=lambda x: (x[0], -x[1]))
processing = 0
maxprocessing = 0
for cargo in cargos:
    if cargo[1] == -1:
        processing += 1
    else:
        processing -= 1
    if processing > 0:
        maxprocessing = max(maxprocessing, processing)
print(maxprocessing)