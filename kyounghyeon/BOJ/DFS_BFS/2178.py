# 제목 : 미로 탐색
# 분류 : BFS, Silver 1
# 출처 : 백준 2178

import collections

n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

def bfs():
    q = collections.deque()
    q.append((0,0,1))
    visited[0][0] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y, d = q.popleft()
        if x == n-1 and y == m-1:
            print(d)
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maze[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx, ny, d + 1))

bfs()

