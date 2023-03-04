# 제목 : 벽 부수고 이동하기
# 분류 : BFS , Gold 3
# 출처 : 백준 2206

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
G = [list(map(int, list(input().strip()))) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
distance = [[[0] * m for _ in range(n)] for _ in range(2)]

def bfs():

    q = deque()
    q.append((0, 0, 0))
    distance[0][0][0] = 1

    while q:
        x, y, hit = q.popleft()
        if x == n-1 and y == m-1:
            return distance[hit][x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if G[nx][ny] == 0 and not distance[hit][nx][ny]:
                    q.append((nx, ny, hit))
                    distance[hit][nx][ny] = distance[hit][x][y] + 1
                elif G[nx][ny] == 1 and not hit:
                    q.append((nx, ny, 1))
                    distance[1][nx][ny] = distance[0][x][y] + 1
    return -1

print(bfs())
