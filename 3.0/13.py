s = input().strip().split()
stack = []

for ch in s:
    if ch not in "+-*":
        stack.append(ch)
    elif stack:
        a = int(stack.pop())
        b = int(stack.pop())
        if ch == "+":
            stack.append(b + a)
        elif ch == "*":
            stack.append(b * a)
        else:
            stack.append(b - a)
if stack:
    print(stack.pop())


