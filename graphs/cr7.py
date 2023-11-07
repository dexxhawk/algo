n, m = map(int, input().split())
n += 1
E = [[] for _ in range(n)]

for i in range(m):
    u, v = map(int, input().split())
    E[u].append(v)
    E[v].append(u)


used = [False] * n
qty = 0
cc = []

def dfs(v: int):
    global qty
    used[v] = True
    qty += 1
    cc.append(v)
    for to in E[v]:
        if used[to] == False:
            dfs(to)
dfs(1)

print(qty)
cc.sort()
print(cc)