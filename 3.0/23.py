n = int(input())

dp = [(10**6 + 1, 10**6 + 1)] * (n + 1)
dp[1] = 0

prev = [-1] * (n + 1)

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1
    prev[i] = i - 1

    if i % 2 == 0 and dp[i // 2] < dp[i]:
        dp[i] = dp[i // 2] + 1
        prev[i] = i // 2
    if i % 3 == 0 and dp[i // 3] < dp[i]:
        dp[i] = dp[i // 3] + 1
        prev[i] = i // 3

print(dp[n])

nums = []
prev_el = n
while prev_el != -1:
    nums.append(prev_el)
    prev_el = prev[prev_el]

for i in range(len(nums) - 1, -1, -1):
    print(nums[i], end=" ")



