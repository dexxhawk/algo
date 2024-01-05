from sys import stdin

dct = {}
words = stdin.read().split()

for word in words:
    if word not in dct:
        dct[word] = 0
    dct[word] += 1

ans = []
for key in dct:
    ans.append((-dct[key], key))

ans.sort()
print(ans)
for elem in ans:
    print(elem[1])
