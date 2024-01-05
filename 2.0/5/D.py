s = list(map(lambda x: 1 if x == "(" else -1 , input()))

cursum = 0
flag = 0
for elem in s:
    cursum += elem
    if cursum < 0:
        flag = 1
        break
if cursum == 0 and not flag:
    print("YES")
else:
    print("NO")



