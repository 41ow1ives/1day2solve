# 제목 : 적록색약
# 분류 : DFS/BFS, Gold 5
# 출처 : 백준 10026

import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
G = [list(input().rstrip()) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j):
    q = deque()
    col = G[i][j]
    q.append((i, j))

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and col == G[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))

cnt1 = 0
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            cnt1 += 1

for i in range(n):
    for j in range(n):
        if G[i][j] == 'G': G[i][j] = 'R'

cnt2 = 0
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            cnt2 += 1

print(cnt1, cnt2)
