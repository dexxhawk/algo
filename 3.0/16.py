class Queue:
    def __init__(self) -> None:
        self.queue = []

    def push(self, n) -> str:
        self.queue.append(n)
        return "ok"

    def pop(self):
        if not self.queue:
            return "error"
        ans = self.queue[0]
        self.queue = self.queue[1::]
        return ans
    
    def front(self):
        if not self.queue:
            return "error"
        return self.queue[0]
    
    def size(self) -> int:
        return len(self.queue)

    def clear(self) -> str:
        self.queue.clear()
        return "ok"


s = input()
queue = Queue()

while s != "exit":
    cmd = s.split()
    match cmd[0]:
        case "push":
            print(queue.push(int(cmd[1])))
        case "pop":
            print(queue.pop())
        case "front":
            print(queue.front())
        case "size":
            print(queue.size())
        case clear:
            print(queue.clear())
    s = input()
print("bye")