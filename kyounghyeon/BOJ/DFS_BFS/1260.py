# 제목 : DFS와 BFS
# 분류 : DFS/BFS, Silver 2
# 출처 : 백준 1260

# 함수
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end='')
    for w in graph[v]:
        if not visited[w]:
            dfs(graph, w, visited)

def bfs(graph, v):
    visited = [False] * (n+1)
    q = collections.deque()
    q.append(v)
    visited[v] = True

    while q:
        w = q.popleft()
        print(w, end=' ')
        for i in graph[w]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

# 실제 구현
n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, len(graph)):
    graph[i].sort()

visited_dfs = [False] * (n+1)
dfs(graph, v, visited_dfs)
print()
bfs(graph, v)

