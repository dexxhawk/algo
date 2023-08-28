n, s = map(int, input().split())
a = list(map(int, input().split()))

l = 0
ans = 0
x = 0 

for r in range(len(a)):
    x += a[r]
    while (x >= s):
        ans += 1
        x -= a[l]
        l += 1
    
    #(i..r) where i = 0..l-1 is good
    # then qty = l
print(ans)
    