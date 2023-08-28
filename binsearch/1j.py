def binsearch(x: int, a: list[int]) -> str:
    l = 0
    r = len(a) - 1
    ans = 0
    while(l <= r):
        mid = (l + r) // 2
        if (a[mid] <= x):
            l = mid + 1
            ans = mid
        else:
            r = mid - 1
    if (a[ans] == x):
        return "YES"
    else:
        return "NO"

n, k = map(int, input().split())
a = list(map(int, input().split()))
req = list(map(int, input().split()))

for now in req:
    print(binsearch(now, a))
