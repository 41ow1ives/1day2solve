import sys
from collections import deque
si = sys.stdin.readline
v = int(si())
nodes = [[] for _ in range(v + 1)]

for _ in range(v):
    tmp = list(map(int, si().split()))
    for i in range(1, len(tmp) - 2, 2):
        nodes[tmp[0]].append((tmp[i], tmp[i + 1]))
        
Q = deque([(1, 0)])
v1, v1_dist = 0, 0
visit = [False] * (v + 1)
while Q:
    x, x_dist = Q.popleft()
    visit[x] = True
    if x_dist >= v1_dist:
        v1 = x
        v1_dist = x_dist
    for y, y_dist in nodes[x]:
        if visit[y]: continue
        Q.append((y, x_dist + y_dist))
        
Q = deque([(v1, 0)])
visit = [False] * (v + 1)
ans = 0
while Q:
    x, x_dist = Q.popleft()
    visit[x] = True
    if x_dist >= ans:
        ans = x_dist
    for y, y_dist in nodes[x]:
        if visit[y]: continue
        Q.append((y, x_dist + y_dist))
        
print(ans)