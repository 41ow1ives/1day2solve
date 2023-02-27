# 제목 : 안전 영역
# 분류 : 그래프 탐색, Silver 1
# 출처 : 백준 2468

import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline
n = int(input())
G = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, rain):

    visited[x][y] = True

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and G[nx][ny] > rain:
                dfs(nx, ny, rain)

m = 1
for rain in range(1, max(max(G))):
    visited = [[False] * n for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and G[i][j] > rain:
                dfs(i, j, rain)
                cnt += 1

    m = max(m, cnt)

print(m)