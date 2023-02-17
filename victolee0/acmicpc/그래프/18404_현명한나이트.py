import sys
from collections import deque
si = sys.stdin.readline

n, m = map(int, si().split())
nx, ny = map(int, si().split())
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]

queue = deque([(nx, ny, 0)])
board = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]

while queue:
    tx, ty, cnt = queue.popleft()
    if board[tx][ty] != -1:
        continue
    board[tx][ty] = cnt

    for i in range(8):
        fx = tx + dx[i]
        fy = ty + dy[i]
        if 0 <= fx < n + 1 and 0 <= fy < n + 1:
            queue.append((fx, fy, cnt + 1))
                
                
for _ in range(m):
    x, y = map(int, si().split())
    print(board[x][y], end = ' ')