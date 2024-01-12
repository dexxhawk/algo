import sys
sys.setrecursionlimit(10 ** 4 + 5 * 10 ** 5)

def dfs(graph: list[list[int]], visited: list[bool], now: int, cc: list[int]):
    visited[now] = True
    cc.append(now)
    for neig in graph[now]:
        if not visited[neig]:
            dfs(graph, visited, neig, cc)

with open ("input.txt", "r") as fin:
    n, m = map(int, fin.readline().split())
    # sys.setrecursionlimit(n + m +1)
    # Прошло, но наверное, лучше задать хардово вначале и с запасом

    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    cc = []

    for i in range(m):
        v, u = map(int, fin.readline().split())
        graph[v].append(u)
        graph[u].append(v)

    dfs(graph, visited, 1, cc)

    cc.sort()
    print(len(cc))
    print(*cc)
