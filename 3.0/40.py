from queue import Queue
import queue

n = int(input())
m = int(input())

sets = [0] * (m + 1)
for i in range(1, m + 1):
    sets[i] = set(list(map(int, input().split()))[1::])

a, b = map(int, input().split())

possible_start_lines = []
possible_end_lines = []
for i in range(1, m + 1):
    if a in sets[i]:
        possible_start_lines.append(i)
    if b in sets[i]:
        possible_end_lines.append(i)

graph = [[] for _ in range(m + 1)]

for i in range(1, m + 1):
    for j in range(i + 1, m + 1):
        changes = sets[i] & sets[j]
        if changes:
            graph[i].append(j)
            graph[j].append(i)


queue = Queue()
dist = [-1] * (m + 1)
for i in range(len(possible_start_lines)):
    dist[possible_start_lines[i]] = 0
    queue.put(possible_start_lines[i])

while not queue.empty():
    now = queue.get()
    for neig in graph[now]:
        if dist[neig] == -1:
            queue.put(neig)
            dist[neig] = dist[now] + 1

ans = m + 1
for i in range(len(possible_end_lines)):
    if 0 <= dist[possible_end_lines[i]] < ans:
        ans = dist[possible_end_lines[i]]
if ans == m + 1:
    print(-1)
else:
    print(ans)

