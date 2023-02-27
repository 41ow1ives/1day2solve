# 제목 : 경로 찾기
# 분류 : 그래프 탐색, Silver 1
# 출처 : 백준 11403

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
Adj = [list(map(int, input().split())) for _ in range(n)]
G = [[] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if Adj[i][j] == 1:
            G[i].append(j)

def bfs(s):

    visited = [0] * n
    q = deque()
    q.append(s)

    while q:
        v = q.popleft()
        for w in G[v]:
            if not visited[w]:
                q.append(w)
                visited[w] = 1

    return visited

result = []
for i in range(n):
    result.append(bfs(i))

for t in result:
    print(' '.join(map(str, t)))