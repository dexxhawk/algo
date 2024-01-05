s = input()
stack = []
flag = 0
for br in s:
    if br in "([{":
        stack.append(br)
    elif br == ")" and stack and stack[-1] == "(":
        stack.pop()
    elif br == "]" and stack and stack[-1] == "[":
        stack.pop()
    elif br == "}" and stack and stack[-1] == "{":
        stack.pop()
    else:
        print("no") 
        flag = 1
        break
if not flag:
    print("yes" if len(stack) == 0 else "no")