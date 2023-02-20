import sys
from collections import deque
si = sys.stdin.readline
n, m = map(int, si().split())

maps = [si().strip() for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

Q = deque([(1, 1, 1)])
visited = [[0] * m for _ in range(n)]
while Q:
    x, y, dist = Q.popleft()
    if visited[x - 1][y - 1]:
        continue
    if maps[x - 1][y - 1] == '0':
        continue
    visited[x - 1][y - 1] = dist
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 1 or nx > n or ny < 1 or ny > m:
            continue
        Q.append((nx, ny, dist + 1))
    
print(visited[n - 1][m - 1])