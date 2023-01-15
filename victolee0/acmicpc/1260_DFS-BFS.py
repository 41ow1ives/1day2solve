import sys

n, m, v = map(int, sys.stdin.readline().strip().split())

adj = {i+1 : [] for i in range(n)}

for i in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    adj[a] += [b]
    adj[b] += [a]

for i in range(1, n+1):
    adj[i].sort()
    
def dfs(lst, visited):
    now = lst.pop(0)
    visited.append(now)
    for i in adj[now]:
        if i in visited:
            continue
        lst.append(i)
        dfs(lst, visited)
    
    return visited


def bfs(lst, visited):
    while lst:
        now = lst.pop(0)
        if now in visited:
            continue
        visited.append(now)
        lst += adj[now]
    
    return visited

a = dfs([v], [])
print(*a)

a = bfs([v], [])
print(*a)