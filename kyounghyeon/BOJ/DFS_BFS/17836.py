# 제목 : 공주님을 구해라!
# 분류 : BFS, Gold 2
# 출처 : 백준 17836

import sys
from collections import deque

input = sys.stdin.readline

N, M, T = map(int, input().split())
G = []
for _ in range(N):
    G.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0] * M for _ in range(N)]


def bfs():
    gram = 100000
    q = deque()
    q.append((0,0))
    visited[0][0] = 1

    while q:
        x, y = q.popleft()

        if G[x][y] == 2:
            gram = visited[x][y] + (M-1-x) + (N-1-y) - 1

        if x == N-1 and y == M-1:
            return min(visited[x][y]-1, gram)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and G[nx][ny] != 1 and visited[nx][ny] == 0:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

    return gram

a = bfs()
if a > T:
    print('Fail')
else:
    print(a)
