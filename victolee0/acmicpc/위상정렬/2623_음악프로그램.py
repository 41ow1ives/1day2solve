import sys
from collections import deque

si = sys.stdin.readline
n, m = map(int, si().split())
con = [[] for _ in range(n + 1)]
indeg = [0] * (n + 1)

for _ in range(m):
    tmp = list(map(int, si().split()))
    for i in range(2, len(tmp)):
        con[tmp[i - 1]].append(tmp[i])
        indeg[tmp[i]] += 1

Q = deque()
for i in range(1, n + 1):
    if indeg[i] == 0:
        Q.append(i)
    
ans = []
while Q:
    now = Q.popleft()
    ans.append(now)
    for i in con[now]:
        indeg[i] -= 1
        if indeg[i] == 0:
            Q.append(i)

if len(ans) == n:
    for i in ans:
        print(i)
else:
    print(0)