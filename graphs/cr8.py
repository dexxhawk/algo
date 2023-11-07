n, m = map(int, input().split())
n += 1
E = [[] for _ in range(n)]

for i in range(m):
    u, v = map(int, input().split())
    E[u].append(v)
    E[v].append(u)

used = [False] * n
allcc = []

def dfs(v: int, cc: list[int]) -> list[int]:
    used[v] = True
    cc.append(v)
    for to in E[v]:
        print("E[v]:", E[v])
        if used[to] == False:
            dfs(to, cc)
    return cc

for i in range(1, n):
    if used[i] == False:
        allcc.append(dfs(i, []))


# print(len(allcc))

# for elem in allcc:
#     print(len(elem))
#     print(*elem)