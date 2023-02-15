# 제목 : 케빈 베이컨의 6단계 법칙
# 분류 : BFS, Silver 1
# 출처 : 백준 1389

from collections import deque

n, m = map(int, input().split())
G = { i+1 : [] for i in range(n)}
for _ in range(m):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

def bfs(s):

    q = deque()
    q.append(s)
    dist = [0] * (n+1)
    visited = [False] * (n+1)
    visited[s] = True

    while q:
        v = q.popleft()
        for w in G[v]:
            if not visited[w]:
                q.append(w)
                visited[w] = True
                dist[w] = dist[v] + 1

    return sum(dist)

kevin_num = []
for i in range(1, n+1):
    kevin_num.append(bfs(i))

print(kevin_num.index(min(kevin_num))+1)