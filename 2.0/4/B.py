from sys import stdin

dct = {}
lines = []
for line in stdin:
    lines.append(line.rstrip("\n"))
    surname, qty = line.rstrip("\n").split()
    if surname not in dct:
        dct[surname] = 0
    dct[surname] += int(qty)

for key in sorted(dct):
    print(key, dct[key])
