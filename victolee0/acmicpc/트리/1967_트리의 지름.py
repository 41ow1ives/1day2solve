import sys
from collections import deque
si = sys.stdin.readline
n = int(si())

con = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, si().split())
    con[a].append((b, c))
    con[b].append((a, c))
    
Q = deque([(1, 0)])
visited = [False for _ in range(n + 1)]
v1, v_dist = None, 0
while Q:
    x, dist = Q.popleft()
    if visited[x]: continue
    visited[x] = True
    if v_dist <= dist:
        v1 = x
        v_dist = dist
    for y, y_dist in con[x]:
        Q.append((y, dist + y_dist))

        
Q = deque([(v1, 0)])
visited = [False for _ in range(n + 1)]
v2, v_dist = None, 0
while Q:
    x, dist = Q.popleft()
    if visited[x]: continue
    visited[x] = True
    if v_dist <= dist:
        v2 = x
        v_dist = dist
    for y, y_dist in con[x]:
        Q.append((y, dist + y_dist))
    

print(v_dist)
