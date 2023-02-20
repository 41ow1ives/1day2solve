# 제목 : 거리두기 확인하기
# 분류 : BFS
# 출처 : 프로그래머스, 2021 kakao internship recruiting

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(G, i, j):
    q = deque()
    q.append((i, j, 0))
    visited = [[False] * 5 for _ in range(5)]

    while q:
        x, y, d = q.popleft()
        visited[x][y] = True
        d += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny] and d <= 2 and G[nx][ny] != 'X':
                if G[nx][ny] == 'P':
                    return False
                else:
                    q.append((nx, ny, d))

    return True


def solution(places):
    answer = []
    for P in places:
        ok = True
        for i in range(5):
            for j in range(5):
                if P[i][j] == 'P':
                    ok = bfs(P, i, j)
                if not ok:
                    break
            if not ok:
                break

        if ok:
            answer.append(1)
        else:
            answer.append(0)

    return answer