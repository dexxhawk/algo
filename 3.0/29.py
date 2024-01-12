
n = int(input())
INF = 300 * n + 1


cost = [0] * (n + 1)
for i in range(1, n + 1):
    cost[i] = int(input())

# dp[i][j] - в i-ый день имеем j купонов, заплатили минимальную сумму dp[i][j]
# BASE
dp = [[INF] * (n + 1) for _ in range(n + 1)]
dp[0][0] = 0

prev = [[-1] * (n + 1) for _ in range(n + 1)]

# Solution:
for i in range(1, n + 1):
    for j in range(n + 1):

        dp[i][j] = dp[i - 1][j] + cost[i]
        prev[i][j] = (i - 1, j)
        if j < n:
            if dp[i][j] > dp[i - 1][j + 1]:
                dp[i][j] = dp[i - 1][j + 1]
                prev[i][j] = (i - 1, j + 1)
        if j > 0 and cost[i] > 100: #Последним рассматривается этот вариант, за счет чего достигается выбор случая с max кол-вом купонов
            if dp[i][j] >= dp[i - 1][j - 1] + cost[i]:
                dp[i][j] = dp[i - 1][j - 1] + cost[i]
                prev[i][j] = (i - 1, j - 1)

min_cost = dp[n][0]
index_of_min = 0
for j in range(1, n + 1):
    if dp[n][j] <= min_cost:
        min_cost = dp[n][j]
        index_of_min = j
print(min_cost)

# знаки >=, чтобы выбирать вариант с максимальным j

k1, k2 = index_of_min, 0
coupon_days = []
cur_i, cur_j = n, index_of_min

for i in range(n):
    if prev[cur_i][cur_j] == (cur_i - 1, cur_j - 1):
        k2 += 1
    elif prev[cur_i][cur_j] == (cur_i - 1, cur_j + 1):
        coupon_days.append(cur_i)
    cur_i, cur_j = prev[cur_i][cur_j]

k2 -= k1

print(k1, k2)
for i in range(k2 - 1, -1, -1):
    print(coupon_days[i])

# Можно было обойтись и без массива prev для восстановления, но с ним проще и понятнее