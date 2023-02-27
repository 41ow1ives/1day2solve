import sys
from collections import deque
si = sys.stdin.readline
n = int(si())
con = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, si().split())
    con[a].append(b)
    con[b].append(a)
    
Q = deque([(1, 0)])
visited = [0] * (n + 1)
val = 0
while Q:
    leaf = True
    x, dist = Q.popleft()
    visited[x] = 1
    
    for y in con[x]:
        if visited[y]:
            continue
        Q.append((y, dist + 1))
        leaf = False
    if leaf:
        val += dist
        
if val % 2 == 1:
    print("Yes")
else:
    print("No")