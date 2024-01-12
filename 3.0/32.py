import sys
sys.setrecursionlimit(10**6)
# 2*10**5 зашло
# и 10**5 тоже...

def dfs(graph, visited, now, cc):
    visited[now] = True
    cc.append(now)
    for neig in graph[now]:
        if not visited[neig]:
            dfs(graph, visited, neig, cc)

with open('input.txt', 'r', encoding='utf-8') as fin:
    n, m = map(int, fin.readline().split())
    graph = [[] for _ in range(n + 1)]
    for i in range(m):
        v, u = map(int, fin.readline().split())
        graph[v].append(u)
        graph[u].append(v)


    cc = []
    visited = [False] * (n + 1)

    for i in range(1, n + 1):
        if not visited[i]:
            cur_cc = []
            dfs(graph, visited, i, cur_cc)
            cc.append(cur_cc)
    
    print(len(cc))
    for comp in cc:
        print(len(comp))
        print(*comp)
