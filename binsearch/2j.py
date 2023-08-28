def bs(x: int, a: list[int]) -> int:
    l = 0
    r = len(a) - 1
    ans = 0

    while l <= r:
        mid = (l + r) // 2
        if a[mid] <= x:
            l = mid + 1
            ans = mid
        else:
            r = mid - 1
            
    if (a[ans] <= x): 
        return ans + 1
    else: 
        return 0


n, k = map(int, input().split())
a = list(map(int, input().split()))
req = list(map(int, input().split()))

for el in req:
    print(bs(el, a))
