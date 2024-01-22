from queue import Queue
import queue
# O(n**3)
n = int(input())


dx = [0, 0, 0, 0, 1, -1]
dy = [0, 0, 1, -1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]
dist = [[[] for _ in range(n)] for _ in range(n)]

start = (0, 0, 0)
for i in range(n):
    input()
    for j in range(n):
        s = list(input())
        for k in range(n):
            if s[k] == '#':
                s[k] = -2
            elif s[k] == '.':
                s[k] = -1
            else:
                s[k] = 0
                start = (i, j, k)
        dist[i][j] = s


queue = Queue()
queue.put(start)

while not queue.empty():
    now = queue.get()
    for i in range(len(dx)):
        neig_x = now[0] + dx[i]
        neig_y = now[1] + dy[i]
        neig_z = now[2] + dz[i]
        if 0 <= neig_x < n and 0 <= neig_y < n and 0 <= neig_z < n and dist[neig_x][neig_y][neig_z] == -1:
            dist[neig_x][neig_y][neig_z] = dist[now[0]][now[1]][now[2]] + 1
            queue.put((neig_x, neig_y, neig_z))

min_ans = n**3
flag = False

for j in range(n):
    for k in range(n):
        if 0 < dist[0][j][k] < min_ans:
            min_ans = dist[0][j][k]
            flag = True
if flag:
    print(min_ans)
else:
    print(-1)




