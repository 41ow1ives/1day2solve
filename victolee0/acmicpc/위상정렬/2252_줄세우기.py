import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

deg = [0 for _ in range(n + 1)]
dic = {i+1 : [] for i in range(n + 1)}
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    dic[a] += [b]
    deg[b] += 1
    
queue = deque([])

for i in range(1, n + 1):
    if deg[i] == 0:
        queue.append(i)
        
while queue:
    now = queue.popleft()
    print(now, end=' ')
    for i in dic[now]:
        deg[i] -= 1
        if deg[i] == 0:
            queue.append(i)
            
