import sys
from collections import deque
si = sys.stdin.readline
n, m = map(int, si().split())
parent = [0] + list(map(int, si().split()))
good = [0] * (n + 1)
con = [[] for _ in range(n + 1)]
for _ in range(m):
    i, w = map(int, si().split())
    good[i] += w

for i in range(n + 1):
    if parent[i] == 0 and parent == -1:
        continue
    con[i].append(parent[i])
    con[parent[i]].append(i)
    
Q = deque([(1, 0)])
visited = [0] * (n + 1)
while Q:
    i, w = Q.popleft()
    visited[i] = 1
    good[i] += w
    for x in con[i]:
        if x == -1 or visited[x]:
            continue
        Q.append((x, good[i]))
        
print(' '.join(str(i) for i in good[1:]))
