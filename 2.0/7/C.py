segs = []
m = int(input())

l, r = map(int, input().split())
while l != 0 or r != 0:
    if r > 0 and l < m:
        segs.append((l, r))
    l, r = map(int, input().split())

segs.sort()
ans = []
nowright = 0
nextright = 0
nowbest = 0, 0


for seg in segs:
    if seg[0] > nowright:
        ans.append(nowbest)
        nowright = nextright
        if nowright >= m:
            break
    if seg[0] <= nowright and seg[1] > nextright:
        nextright = seg[1]
        nowbest = seg
# Взаимоисключающие условия. Если будет ситуация [0,1], [2, 4], то
# Мы не зайдем во второе условие (23), пожтому не дойдем до конца
# Решения не будет

# Last iteration if the best exists:
# Тк в цикле выполнится условие 23, но чтобы добавить лучший отрезок,
# Нужна еще одна итерация, которой нет
if nowright < m:
    nowright = nextright
    ans.append(nowbest)
# If not enough:
if nowright < m:
    print("No solution")
else:
    print(len(ans))
    for seg in ans:
        print(*seg)