def findl(a, x):
    l = -1
    r = len(a) - 1
    while r > l + 1:
        m = (l + r) // 2
        if (a[m] >= x):
            r = m
        else:
            l = m
    if a[r] == x:
        return r
    return -1

def findr(a, x):
    l = 0
    r = len(a)
    while r > l + 1:
        m = (l + r) // 2
        if (a[m] > x):
            r = m
        else:
            l = m
    if a[l] == x:
        return l
    return -1


n = int(input())
a = list(map(int, input().split()))
m = int(input())
q = list(map(int, input().split()))

for elem in q:
    l, r = findl(a, elem) + 1, findr(a, elem) + 1
    print(l, r)
