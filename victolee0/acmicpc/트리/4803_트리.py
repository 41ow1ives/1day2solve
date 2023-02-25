import sys
from collections import deque

def dfs(x):
    global n_node
    global n_edge
    if nodes[x]:
        return
    nodes[x] += 1
    n_node += 1
    n_edge += len(con[x])
    for y in con[x]:
        dfs(y)
        
si = sys.stdin.readline
idx = 1
while True:
    n, m = map(int, si().split())
    if n == 0 and m == 0:
        break
    con = [[] for _ in range(n + 1)]
    nodes = [0] * (n + 1)
    ans = 0
    for _ in range(m):
        a, b = map(int, si().split())
        con[a].append(b)
        con[b].append(a)

    for i in range(1, n + 1):
        if nodes[i]:
            continue
        n_node = 0
        n_edge = 0
        dfs(i)
        if 2 * (n_node - 1) == n_edge:
            ans += 1
    if ans == 0:
        print(f'Case {idx}: No trees.')
    elif ans == 1:
        print(f'Case {idx}: There is one tree.')
    else:
        print(f'Case {idx}: A forest of {ans} trees.')
    idx += 1
