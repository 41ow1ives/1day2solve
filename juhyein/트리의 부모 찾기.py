n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a]+=[b]
    graph[b]+=[a]

p = [0]*(n+1)
visited = [False]*(n+1)

from collections import deque

def dfs(graph, s, visited):
    visited[s] = True
    stack = deque([s])
    while stack:
        x=stack.pop()
        for i in graph[x]:
            if not visited[i]:
                stack.append(i)
                visited[i]=True
                p[i]=x
                
dfs(graph,1,visited)
for i in range(2,n+1):
        print(p[i])

