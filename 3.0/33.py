# O(V+E)
import sys
sys.setrecursionlimit(10**6)
COLORS_QTY = 3

def dfs(graph, visited, now, color) -> bool:
    visited[now] = color
    for neig in graph[now]:
        if visited[neig] == color:
            return False
        elif visited[neig] == 0 and not dfs(graph, visited, neig, COLORS_QTY - color):
                return False
    return True

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for i in range(m):
    v, u = map(int, input().split())
    graph[v].append(u)
    graph[u].append(v)

visited = [0] * (n + 1)


flag = True
for i in range(n):
    if not visited[i]:
        flag = flag and dfs(graph, visited, i, 1)

print("YES" if flag else "NO")




