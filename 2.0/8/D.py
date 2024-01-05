import sys
sys.setrecursionlimit(2501)

# Идея: рекурсивно считаем для каждого поддерева максимальную глубину и 
# маскимальную длину пути(диаметр)

def dfs(v: int, E: list[int], used: list[bool], maxdepth: list[int]):
    used[v] = True
    best = 1
    max1 = 0
    max2 = 0
    maxdepth[v] = 1

    for next in E[v]:
        if not used[next]:
            best = max(dfs(next, E, used, maxdepth), best)
            if maxdepth[next] > max1:
                max2 = max1
                max1 = maxdepth[next]
            elif maxdepth[next] > max2:
                max2 = maxdepth[next]

    best = max(best, max1 + max2 + 1) #maxdiam
    maxdepth[v] = max(maxdepth[v], max1 + 1)
    return best


n = int(input())
E = [[] for _ in range(n + 1)] #Список смежности

for i in range(n - 1):
    v, u = map(int, input().split())
    E[v].append(u)
    E[u].append(v)

maxdepth = [0] * (n + 1)
used = [False] * (n + 1)


print(dfs(1, E, used, maxdepth))