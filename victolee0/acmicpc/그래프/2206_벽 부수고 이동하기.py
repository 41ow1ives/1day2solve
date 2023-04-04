import sys
from collections import deque
si = sys.stdin.readline
n, m = map(int, si().split())
maps = [si().strip() for _ in range(n)]

dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

Q = deque([(0, 0, 1, True)])
dist = [[[-1, -1] for _ in range(m)] for _ in range(n)]
while Q:
    x, y, d, possible = Q.popleft()
    if possible and dist[x][y][0] == -1:
        dist[x][y][0] = d
    elif possible and dist[x][y][0] > d:
        dist[x][y][0] = d
    elif not possible and dist[x][y][1] == -1:
        dist[x][y][1] = d
    elif not possible and dist[x][y][1] > d:
        dist[x][y][1] = d
    else:
        continue
    for i in range(4):
        nx = x + dxy[i][0]
        ny = y + dxy[i][1]
        if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
        if possible and maps[nx][ny] == '1':
            Q.append((nx, ny, d + 1, False))
        if maps[nx][ny] == '0':
            Q.append((nx, ny, d + 1, possible))
a, b = dist[n-1][m-1]
if a == -1:
    print(b)
elif b == -1:
    print(a)
else:
    print(min(dist[n-1][m-1]))
