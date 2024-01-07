from collections import deque

s = input().split()

deq = deque()

while s[0] != "exit":
    match s[0]:
        case "push_front":
            deq.appendleft(int(s[1]))
            print("ok")
        case "push_back":
            deq.append(int(s[1]))
            print("ok")
        case "pop_front":
            if not deq:
                print("error")
            else:
                print(deq.popleft())
        case "pop_back":
            if not deq:
                print("error")
            else:
                print(deq.pop())
        case "front":
            if not deq:
                print("error")
            else:
                print(deq[0])
        case "back":
            if not deq:
                print("error")
            else:
                print(deq[-1])
        case "size":
            print(len(deq))
        case clear:
            deq.clear()
            print("ok")

    s = input().split()
print("bye")