# O(V+E)
import sys
sys.setrecursionlimit(10**6)

def dfs(graph, visited, now, arr):
    visited[now] = 1
    for neig in graph[now]:
        if visited[neig] == 1:
            return False
        elif not visited[neig]:
            if not dfs(graph, visited, neig, arr):
                return False
    visited[now] = 2
    arr.append(now)
    return True


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for i in range(m):
    v, u = map(int, input().split())
    graph[v].append(u)

visited = [0] * (n + 1)

arr = []
flag = True
for i in range (1, n + 1):
    if not visited[i]:
        if not dfs(graph, visited, i, arr):
            flag = False
            break
if flag:
    print(*arr[::-1])
else:
    print(-1)