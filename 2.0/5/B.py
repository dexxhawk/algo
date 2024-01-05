n = int(input())
a = list(map(int, input().split()))

pref = [0] * (n + 1)
for i in range(1, n + 1):
    pref[i] = pref[i - 1] + a[i - 1]

maxsum = pref[1]
minpref = pref[0]
for i in range(2, n + 1):
    minpref = min(minpref, pref[i - 1])
    maxsum = max(maxsum, pref[i] - minpref)
print(maxsum)