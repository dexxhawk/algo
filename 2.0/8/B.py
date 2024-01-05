# Через дерево решается так же в 2 прохода

from sys import stdin

n = int(input())

dct = {}
for i in range(n - 1):
    s = input().split()
    dct[s[0]] = s[1]



for line in stdin:
    key, val = line.rstrip("\n").split()

    cur_key = key
    flag = 0
    while not flag and cur_key in dct:
        if dct[cur_key] == val:
            print(2, end=" ")
            flag = 1
            break
        cur_key = dct[cur_key]
        
    cur_key, val = val, key

    while not flag and cur_key in dct:
        if dct[cur_key] == val:
            print(1, end=" ")
            flag = 1
            break
        cur_key = dct[cur_key]

    if not flag:
        print(0, end=" ")


        
