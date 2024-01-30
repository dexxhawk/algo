def find(a: list[int], n: int, b: list[int], m: int) -> int:
    dct1={}
    dct2={}

    for elem in a:
        if elem not in dct1:
            dct1[elem] = 0
        dct1[elem] += 1
    
    for elem in b:
        if elem not in dct2:
            dct2[elem] = 0
        dct2[elem] += 1

    i = 0
    j = 0
    cnt = 0

    while j < m and i < n:
        if a[i] < b[j]:
            i += 1
        elif a[i] > b[j]:
            j += 1
        else:
            cnt += max(dct1[a[i]], dct2[b[j]])
            i += 1
            j += 1
    return cnt



n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(find(a, n, b, m))