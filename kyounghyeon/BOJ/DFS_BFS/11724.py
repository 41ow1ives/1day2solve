# 제목 : 연결요소의 개수
# 분류 : DFS/BFS, Silver 2
# 출처 : 백준 11724

import sys
sys.setrecursionlimit(10000)

def dfs(graph, start):
    visited[start] = True
    for v in graph[start]:
        if not visited[v]:
            dfs(graph, v)

n, m = map(int, sys.stdin.readline().split())
G = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    G[a].append(b)
    G[b].append(a)

visited = [False] * (n+1)
cnt = 0
while True:
    start = visited[1:].index(False)+1
    dfs(G, start)
    cnt += 1
    if sum(visited[1:]) == (len(G)-1):
        break

print(cnt)