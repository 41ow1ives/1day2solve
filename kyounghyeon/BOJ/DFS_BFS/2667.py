# 제목 : 단지번호붙이기
# 분류 : DFS/BFS, Silver 1
# 출처 : 백준 2667

import collections

n = int(input())
apart = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

def bfs(G, a, b): # 시작 지점 입력
    q = collections.deque()
    q.append((a,b))
    visited[a][b] = True # 해당 아파트 방문 (= count)

    dx = [-1, 1, 0, 0] # x가 이동할 좌표
    dy = [0, 0, -1, 1] # y가 이동할 좌표
    count = 1
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x+dx[i] # 좌우
            ny = y+dy[i] # 상하

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and G[nx][ny] == 1:
                # 아파트 범위 내에 있고, 아파트가 있을 때
                # 해당 아파트 좌표 큐에 추가, 방문, 카운트
                q.append((nx, ny))
                visited[nx][ny] = True
                count += 1

    return count # 한 아파트 지역의 개수 return

cnt_lst = []
for i in range(n):
    for j in range(n):
        if not visited[i][j] and apart[i][j] == 1:
            cnt_lst.append(bfs(apart, i, j))

cnt_lst.sort()
print(len(cnt_lst))
for i in range(len(cnt_lst)):
    print(cnt_lst[i])