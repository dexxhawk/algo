n = int(input())
wagons = list(map(int, input().split()))

stack = []
nowmin = 1

for wagon in wagons:
    stack.append(wagon)
    while stack and stack[-1] == nowmin:
        stack.pop()
        nowmin += 1

print("YES" if not stack else "NO") 


















# for wagon in wagons:
#     while 



#     if wagon == nowmin:
#         nowmin += 1
#         continue

#     while stack and stack[-1] == wagon + 1:
#         stack.pop()

# print ("NO" if stack else "YES")