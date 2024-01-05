from sys import stdin

votedct = {}
qty = 0

for line in stdin:
    words = line.split()
    cur_qty = int(words[-1])
    qty += cur_qty
    name = " ".join(words[:-1])
    if name not in votedct:
        votedct[name] = 0
    votedct[name] = cur_qty

qty /= 450

sumqty = 0
fractions = []
placedct = {}
for key in votedct:
    placedct[key] = votedct[key] // qty
    sumqty += placedct[key]
    fractions.append((-((votedct[key] / qty) % 1), votedct[key], key))

if sumqty < 450:
    sorted_fractions = sorted(fractions)
    i = 0
    while(sumqty < 450):
        if i == len(placedct):
            i = 0
        placedct[sorted_fractions[i][2]] += 1
        i += 1
        sumqty +=1

for elem in fractions:
    print(elem[2], int(placedct[elem[2]]))
        


