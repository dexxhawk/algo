def findl(a, L):
    l = -1
    r = len(a)
    while r > l + 1:
        m = (l + r) // 2
        if a[m] >= L:
            r = m
        else:
            l = m
    return r

def findr(a, R):
    l = -1
    r = len(a)
    while r > l + 1:
        m = (l + r) // 2
        if a[m] <= R:
            l = m
        else:
            r = m
    return l
    

n = int(input())
a = list(map(int, input().split()))
k = int(input())

a.sort()
ans = [0] * k

for i in range(k):
    l, r = map(int, input().split())
    ans[i] = findr(a, r) - findl(a, l) + 1
    # If there are no such items, findr will return -1, findl 0
    # then ans[i] = 0
print(*ans) 