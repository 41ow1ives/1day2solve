import sys
from collections import deque
si = sys.stdin.readline

m, n, h= map(int, si().split())

box = []
for _ in range(h):
    tmp = []
    for _ in range(n):
        line = list(map(int, si().split()))
        tmp.append(line)
    box.append(tmp)

dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dh = [0, 0, 0, 0, 1, -1]

dist = [[[-1] * m for _ in range(n)] for _ in range(h)]
Q = deque([])
#h x y
for v in range(h):
    for x in range(n):
        for y in range(m):
            if box[v][x][y] == 1:
                dist[v][x][y] = 0
                Q.append((v, x, y))
            

while Q:
    v, x, y = Q.popleft()
    
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nv = v + dh[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m or nv < 0 or nv >= h:
            continue
        if dist[nv][nx][ny] != -1:
            continue
    
        if box[nv][nx][ny] == 0:
            Q.append((nv, nx, ny))
            dist[nv][nx][ny] = dist[v][x][y] + 1
ans = 0
for v in range(h):
    for x in range(n):
        for y in range(m):
            if box[v][x][y] == -1:
                continue
            if dist[v][x][y] == -1:
                ans = -1
            if ans == -1:
                continue
            ans = max(ans, dist[v][x][y])
            
print(ans)