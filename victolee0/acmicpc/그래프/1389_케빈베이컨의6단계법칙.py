import sys
from collections import deque

si = sys.stdin.readline
n, m = map(int, si().split())
con = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, si().split())
    con[a].append(b)
    con[b].append(a)
    
auser = -1
anum = 5001
for i in range(1, n + 1):
    Q = deque()
    visited = [0] * (n + 1)
    dist = [0] * (n + 1)
    Q.append((i, 0))
    while Q:
        node, weight = Q.popleft()
        if visited[node]:
            continue
        visited[node] = 1
        dist[node] = weight
        for cur in con[node]:
            Q.append((cur, weight + 1))
    s = sum(dist)
    if s < anum:
        auser = i
        anum = s
    
print(auser)
