# 시간초과
M,N = map(int, input().split())
graph = [[] for _ in range(M+1)]
visited = [False]*(M+1)
count = 0

for _ in range(N):
    u,v = map(int, input().split())
    graph[u] += [v]
    graph[v] += [u]
    
from collections import deque
def bfs(v):
    q = deque([v])
    while q:
        x = q.popleft()
        visited[x] = True
        for i in graph[x]:
            if visited[i] == False:
                visited[i] = True
                q.append(i)
                
for i in range(1, M+1):
    if visited[i] == False:
        bfs(i)
        count += 1
        
        
        
