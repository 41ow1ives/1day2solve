import sys
from collections import deque

t = int(sys.stdin.readline().strip())
for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    d = [0] + list(map(int, sys.stdin.readline().split()))
    
    done = [0 for _ in range(n + 1)]
    deg = [0 for _ in range(n + 1)]
    con = [[] for _ in range(n + 1)]

    for i in range(k):
        x, y = map(int, sys.stdin.readline().split())
        deg[y] += 1
        con[x].append(y)
        
    queue = deque([])

    for i in range(1, n + 1):
        if deg[i] == 0:
            queue.append(i)
            done[i] = d[i]
            
    while queue:
        now = queue.popleft()
        for i in con[now]:
            deg[i] -= 1
            if deg[i] == 0:
                queue.append(i)
            done[i] = max(done[i], d[i] + done[now])

    w = int(sys.stdin.readline().strip())
    print(done[w])