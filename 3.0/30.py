n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

# dp[i][j] - максимальная длина НОП, когад взяли i символов из 1-ой строки и 
# j символов из 2-ой строки
dp = [[0] * (m + 1) for i in range(n + 1)]

#BASE:
dp[0][0] = 0

# Solution:
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            
i, j = n, m
subseq = []

while i > 0 and j > 0:
    if dp[i][j] == dp[i - 1][j]:
        i -= 1
    elif dp[i][j] == dp[i][j - 1]:
        j -= 1
    else:
        subseq.append(a[i - 1])
        i -= 1
        j -= 1
print(*subseq[::-1])

# Короче говоря, смотрим ситауцию в клетке dp[i][j]: Если 2 символа совпадают, то длина НОП =  dp[i - 1][j - 1] + 1
# Иначе выбираем наибольшую НОП из max(dp[i - 1][j], dp[i][j - 1]), тк в dp[i][j] мы могли прийти только 2 путями(если буквы i и j не совпали),
# Выбрали максимальную длину суффикса и идем дальше, то что раньше, уже не в нашей влсати
# Ответ в dp[n][m]

