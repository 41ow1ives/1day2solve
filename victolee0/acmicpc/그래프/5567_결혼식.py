import sys
from collections import deque

si = sys.stdin.readline
n = int(si())
m = int(si())
con = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, si().split())
    con[a].append(b)
    con[b].append(a)
    
Q = deque([(1, 0)])
ans = 0
while Q:
    x, dist = Q.popleft()
    if visited[x]:
        continue
    if dist > 2:
        continue
    visited[x] += 1
    ans += 1
    for y in con[x]:
        Q.append((y, dist + 1))    

print(ans - 1)
    