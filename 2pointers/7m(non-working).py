import sys

class stack:

    s = [] 
    smin = []
    smax = []

    def push (self, x: int) -> None:
       self.s.append(x)
       self.smin.append(x if not self.smin else min(self.smin[-1], x))
       self.smax.append(x if not self.smax else max(self.smax[-1], x))  
        
    def pop(self) -> int:
        res = self.s[-1]
        self.s.pop()
        self.smin.pop()
        self.smax.pop()
        return res
        
    def empty(self) -> bool:
        return (True if not self.s else False)
    
    def min(self) -> int:
        return (sys.maxsize if not self.smin else self.smin[-1])

    def max(self) -> int:
        return (- sys.maxsize - 1 if not self.smax else self.smax[-1])


s1, s2 = stack(), stack()
n, k = map(int, input().split())


def add(x: int):
    global s2
    s2.push(x)

def remove():
    global s1, s2
    if s1.empty():
        while not s2.empty():
            s1.push(s2.pop())
    s1.pop()

def good() -> bool:
    global k
    mx = max(s1.max(), s2.max())
    mn = min(s1.min(), s2.min())
    return mx - mn <= k


a = list(map(int, input().split()))

l = 0
res = 0
for r in range(n):
    add(a[r])
    while not good():
        remove()
        l += 1
    res += r - l + 1

print(res)
