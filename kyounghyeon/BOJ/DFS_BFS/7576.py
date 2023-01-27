# 제목 : 토마토
# 분류 : BFS, Gold 5
# 출처 : 백준 7576

from collections import deque

m, n = map(int, input().split())
tomato_mat = [list(map(int, input().split())) for _ in range(n)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(G):

    q = deque()
    day = 0

    for i in range(n):
        for j in range(m):
            if G[i][j] == 1:
                q.append((i,j,0))

    while q:
        x, y, day = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and G[nx][ny] == 0:
                q.append((nx, ny, day + 1))
                G[nx][ny] = 1

    return day

max_day = bfs(tomato_mat)

success = True
for tomato in tomato_mat:
    if 0 in tomato:
        success = False

if success:
    print(max_day)
else:
    print(-1)