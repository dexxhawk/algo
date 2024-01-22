from calendar import c
from collections import deque

n = int(input())

graph = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    s = list(map(int, input().split()))
    for j in range(n):
        if s[j] == 1:
            graph[i].append(j + 1)

start, end = map(int, input().split())

used = [-1] * (n + 1)
used[start] = 0

queue = deque()
queue.append(start)

while queue:
    now = queue.popleft()
    for neig in graph[now]:
        if used[neig] == -1:
            used[neig] = used[now] + 1
            queue.append(neig)
print(used[end])







