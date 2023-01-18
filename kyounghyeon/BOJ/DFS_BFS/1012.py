# 제목 : 유기농 배추
# 분류 : DFS/BFS, Silver 2
# 출처 : 백준 1012

import sys
sys.setrecursionlimit(10**6)

def dfs(G, x, y):

    G[x][y] = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and G[nx][ny] == 1:
            dfs(G, nx, ny)

t = int(input())
count_lst = []
for _ in range(t):

    n, m, k = map(int, sys.stdin.readline().split())
    bachu = [[0]*m for _ in range(n)]

    for _ in range(k):
        a, b = map(int, sys.stdin.readline().split())
        bachu[a][b] = 1


    count = 0
    for i in range(n):
        for j in range(m):
            if bachu[i][j] == 1:
                dfs(bachu, i, j)
                count += 1

    count_lst.append(count)

for i in range(t):
    print(count_lst[i])
