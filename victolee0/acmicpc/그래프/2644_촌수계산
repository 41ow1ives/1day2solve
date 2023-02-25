import sys
from collections import deque
si = sys.stdin.readline
n = int(si())
a, b = map(int, si().split())
m = int(si())
con = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, si().split())
    con[x].append(y)
    con[y].append(x)
    
Q = deque([(a, 0)])
impossible = True
while Q:
    x, dist = Q.popleft()
    if visited[x]:
        continue
    visited[x] = 1
    if x == b:
        print(dist)
        impossible = False
        break
    for y in con[x]:
        Q.append((y, dist + 1))

if impossible:
    print(-1)