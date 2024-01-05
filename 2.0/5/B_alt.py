n = int(input())
a = list(map(int, input().split()))

maxsum = cursum = a[0]
minpref = 0
for i in range(1, n):
    minpref = min(minpref, cursum)
    cursum += a[i]
    maxsum = max(maxsum, cursum - minpref)
print(maxsum)