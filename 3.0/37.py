import queue

n = int(input())

graph = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    s = list(map(int, input().split()))
    for j in range(n):
        if s[j] == 1:
            graph[i].append(j + 1)

start, end = map(int, input().split())

dist = [-1] * (n + 1)
dist[start] = 0
prev = [-1] * (n + 1)

queue = queue.SimpleQueue()
queue.put(start)
while not queue.empty():
    now = queue.get()
    for neig in graph[now]:
        if dist[neig] == -1:
            dist[neig] = dist[now] + 1
            prev[neig] = now
            queue.put(neig)
print(dist[end])

if dist[end] > 0:
    cur_elem = end
    path = []
    for i in range(dist[end] + 1): #Раз уж известна длина кратчайшего пути
        path.append(cur_elem)
        cur_elem = prev[cur_elem]

    for i in range(len(path) - 1, -1, -1):
        print(path[i], end=' ')


