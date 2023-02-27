# 제목 : 토마토
# 분류 : BFS, Gold 5
# 출처 : 백준 7569

from collections import deque

m, n, h = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs(G):

    q = deque()
    day = 0
    for k in range(h):
        for i in range(n):
            for j in range(m):
                if G[k][i][j] == 1:
                    q.append((k, i, j, 0))

    while q:
        z, x, y, day = q.popleft()
        for k in range(6):
            nx = x + dx[k]
            ny = y + dy[k]
            nz = z + dz[k]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and G[nz][nx][ny] == 0:
                q.append((nz, nx, ny, day + 1))
                G[nz][nx][ny] = 1

    return day

max_day = bfs(tomato)

success = True
for to in tomato:
    for t in to:
        if 0 in t:
            success = False
            break

if success:
    print(max_day)
else:
    print(-1)
