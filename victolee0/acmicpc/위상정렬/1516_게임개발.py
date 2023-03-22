import sys
from collections import deque
si = sys.stdin.readline
n = int(si())
indeg = [0] * (n + 1)
times = [0] * (n + 1)
done = [0] * (n + 1)
con = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    inp = list(map(int, si().split()))
    t = inp.pop(0)
    times[i] = t
    indeg[i] = len(inp)
    if len(inp) == 1:
        continue
    for j in inp:
        if j == -1:
            continue    
        con[j] += [i]
    
Q = deque([])
for i in range(n + 1):
    if indeg[i] == 1:
        Q.append(i)
        done[i] = times[i]

while Q:
    x= Q.popleft()
    for y in con[x]:
        indeg[y] -= 1
        if indeg[y] == 1:
            Q.append(y)
        done[y] = max(done[y], done[x] + times[y])
            
for i in range(1, n + 1):
    print(done[i])