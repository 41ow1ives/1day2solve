import sys
from collections import deque
si = sys.stdin.readline

r, c = map(int, si().split())
maps = [list(si().strip()) for _ in range(r)]

dx = [0, 0, 1, -1]
dy= [1, -1, 0, 0]

Q = deque()
water = deque()
for i in range(r):
    for j in range(c):
        if maps[i][j] == 'S':
            Q.append((i, j, 0))
        if maps[i][j] == 'D':
            beaver = (i, j)
        if maps[i][j] == '*':
            water.append((i, j, 0))

dist = [[-1 for _ in range(c)] for _ in range(r)]
water_dist = [[-1 for _ in range(c)] for _ in range(r)]

while water:
    wx, wy, wt = water.popleft()
    if water_dist[wx][wy] != -1:
        continue
    water_dist[wx][wy] = wt
    for i in range(4):
        nwx = wx + dx[i]
        nwy = wy + dy[i]
        if nwx < 0 or nwx >= r or nwy < 0 or nwy >= c: continue
        if maps[nwx][nwy] == 'X': continue
        if maps[nwx][nwy] == 'D': continue 
        
        water.append((nwx, nwy, wt + 1))

while Q:
    x, y, t = Q.popleft()
    if dist[x][y] != -1:
        continue
    
    if maps[x][y] == '*':
        continue
    if water_dist[x][y] != -1 and water_dist[x][y] <= t:
        continue
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= r or ny < 0 or ny >= c: continue
        if maps[nx][ny] == 'X': continue
        if maps[nx][ny] == '*': continue
        Q.append((nx, ny, t + 1))
    dist[x][y] = t
        
    
if dist[beaver[0]][beaver[1]] == -1:
    print("KAKTUS")
else:
    print(dist[beaver[0]][beaver[1]])
    
