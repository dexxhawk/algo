m = int(input())
clues = [0] * m
for i in range(m):
    clues[i] = set(input())

n = int(input())
suspects = [(0, 0)] * n
for i in range(n):
    s = input()
    suspect = set(s)
    qty = 0
    for j in range(m):
        if clues[j] <= suspect:
            qty += 1
    suspects[i] = (qty, s)

    
mxm = max(suspects)[0]

for elem in suspects:
    if elem[0] == mxm:
        print(elem[1])


# m = int(input())
# readings = [set()] * m
# for i in range(m):
#     readings[i] = set(map(str, input()))
# n = int(input())
# # dct = dict()
# dct = [("", 0) for _ in range(n)]
# susp_list = [""] * n
# for i in range(n):
#     s = input()
#     suspect = set(s)
#     for j in range(m):
#         if readings[j] <= suspect:
#             if s not in dct:
#                 dct[s] = 0
#             dct[s] += 1

# mxm = max(dct)

# for key in dct:
#     if dct[key] == dct[mxm]:
#         print(key)



