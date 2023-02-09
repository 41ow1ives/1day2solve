import sys
from collections import deque

si = sys.stdin.readline
m, n = map(int, si().split())

box = [list(map(int, si().split())) for _ in range(n)]
day = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    global day
    queue = deque()

    for i in range(n):
        for j in range(m):
            if box[i][j] == 1:
                queue.append((i, j, 0))
                
    while queue:
        x, y, day = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if box[nx][ny] == 0:
                box[nx][ny] = 1
                queue.append((nx, ny, day + 1))

bfs()
for lst in box:
    if 0 in lst:
        print('-1')
        break
else:
    print(day)
