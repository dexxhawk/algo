n = int(input())

reply = [0] * n
themes = [''] * n
dct = {}

for i in range(n):
    num = int(input())
    if num == 0:
        themes[i] = input()
        reply[i] = i
        dct[i] = dct.get(i, 0) + 1
        input() #msg
    else:
        reply[i] = reply[num - 1]
        dct[reply[i]] = dct.get(reply[i], 0) + 1
        input() #msg

res = []
for key in dct:
    res.append((-dct[key], key))
print(themes[min(res)[1]])