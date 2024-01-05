
def push(n: int) -> str:
    stack.append(n)
    return "ok"

def back():
    if len(stack) == 0:
        return "error"
    return stack[-1]

def size() -> int:
    return len(stack)

def clear() -> str:
    stack.clear()
    return "ok"

def pop() -> int:
    if len(stack) == 0:
        return "error"
    return stack.pop()

stack = []

s = input()
while (s != "exit"):
    s = s.split()
    if s[0] == "push":
        print(push(s[1]))
    elif s[0] == "back":
        print(back())
    elif s[0] == "size":
        print(size())
    elif s[0] == "pop":
        print(pop())
    else:
        print(clear())
    s = input()
print("bye")
    

