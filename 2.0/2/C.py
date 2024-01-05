s = input()
ans = 0
for i in range (len(s) // 2):
    if not s[i] == s[len(s) - i - 1]:
        ans += 1
print(ans)