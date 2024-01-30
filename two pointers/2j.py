

def find(a: list[int], n: int, b: list[int], m: int) -> None:
    i = 0
    for j in range(m):
        while (i < n and a[i] < b[j]):
            i += 1
        print(i, end=' ')

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
find(a, n, b, m)