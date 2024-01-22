from queue import Queue
# Несколько начал и один конец
# O(nm + q), V ~ n * m, E ~ 4nm
n, m, s, t, q = map(int, input().split())

dx = [1, 1, -1, -1, 2, 2, -2, -2]
dy = [-2, 2, -2, 2, -1, 1, -1, 1]

dist = [[-1] * (m + 1) for _ in range(n + 1)]
dist[s][t] = 0
fleas = [(0, 0)] * q

for i in range(q):
    x, y = map(int, input().split())
    fleas[i] = (x, y)

queue = Queue()
queue.put((s, t))

while not queue.empty():
    now = queue.get()
    for i in range(len(dx)):
        neig_x = now[0] + dx[i]
        neig_y = now[1] + dy[i]
        if 0 < neig_x < n + 1 and 0 < neig_y < m + 1 and dist[neig_x][neig_y] == -1:
            queue.put((neig_x, neig_y))
            dist[neig_x][neig_y] = dist[now[0]][now[1]] + 1

ans = 0
flag = True
for i in range(q):
    if dist[fleas[i][0]][fleas[i][1]] != -1:
        ans += dist[fleas[i][0]][fleas[i][1]]
    else:
        flag = False
        break
if flag:
    print(ans)
else:
    print(-1)
