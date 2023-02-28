import sys
si = sys.stdin.readline
n, m = map(int, si().split())
con = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, dist = map(int, si().split())
    con[a].append((b, dist))
    con[b].append((a, dist))
    
def dfs(x, prev, goal, dist):
    if x == goal:
        print(dist)
        return
    for y, w in con[x]:
        if y == prev:
            continue
        dfs(y, x, goal, dist + w)
for _ in range(m):
    checked = [0] * (n + 1)
    a, b = map(int, si().split())
    dfs(a, -1, b, 0)
    