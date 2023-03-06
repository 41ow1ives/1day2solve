import sys
from collections import deque

si = sys.stdin.readline
t = int(si())
for _ in range(t):
    k, m, p = map(int, si().split())
    con = [[] for _ in range(m + 1)]
    indeg = [0] * (m + 1)
    for i in range(p):
        a, b = map(int, si().split())
        con[a].append(b)
        indeg[b] += 1
    
    Q = deque()
    
    val = [0] * (m + 1)
    visited = [0] * (m + 1)
    cnt = [0] * (m + 1)
    
    for i in range(1, m + 1):
        if indeg[i] == 0:
            Q.append(i)
            val[i] = 1
            cnt[i] = 1
        
    ans = 0
    while Q:
        x = Q.popleft()
        if cnt[x] >= 2:
            val[x] += 1
        ans = max(ans, val[x])
        visited[x] = 1
        for y in con[x]:
            if visited[y]:
                continue
            indeg[y] -= 1
            if indeg[y] == 0:
                Q.append(y)
            if val[x] == val[y]:
                cnt[y] += 1
            if val[y] < val[x]:
                val[y] = val[x]
                cnt[y] = 1
    
    print(k, ans)