# 제목 : 바이러스
# 분류 : DFS/BFS, Silver 3
# 출처 : 백준 2606

import collections

n = int(input())
k = int(input())
virus = {i+1 : [] for i in range(n)}
for _ in range(k):
    a, b = map(int, input().split())
    virus[a] += [b]
    virus[b] += [a]

visited = [False] * n

def bfs(G):
    q = collections.deque()
    q.append(1)
    visited[0] = True
    count = 0

    while q:
        v = q.popleft()
        for i in G[v]:
            if not visited[i-1]:
                q.append(i)
                visited[i-1] = True
                count += 1

    return count

print(bfs(virus))