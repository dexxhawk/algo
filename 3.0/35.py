# O(V^2 + E)
from inspect import stack
from operator import index
import sys
sys.setrecursionlimit(500 + 2500)

def dfs(graph, visited, now, prev, stack):
    visited[now] = 1
    stack.append(now)
    for neig in graph[now]:
        if visited[neig] == 1 and neig != prev:
            stack.append(neig)
            return True
        elif not visited[neig]:
            if dfs(graph, visited, neig, now, stack):
                return True
    stack.pop()
    visited[now] = 2
    return False

n = int(input())

graph = [[] for _ in range(n + 1)] #С этим работать приятнее
# + можно было считывать половину таблицы, тк неор. граф, но это неасимптот. оптимизация.
for i in range(1, n + 1):
    s = list(map(int, input().split()))
    for j in range(len(s)):
        if s[j] == 1:
            graph[i].append(j + 1)

visited = [0] * (n + 1)

path = []
flag = False
for i in range(1, n + 1):
    if not visited[i]:
        path = []
        if dfs(graph, visited, i, i, path):
            flag = True
            break
    
if flag:
    print("YES")

    last_el = path.pop()
    first_el_idx = 0
    for i in range(len(path) - 1): #В приниципе, цикл в неор.графе состоит из 3 вершин и больше
        if path[i] == last_el:
            first_el_idx = i

    ans = path[first_el_idx::]
    print(len(ans))
    print(*ans)
else:
    print("NO")



