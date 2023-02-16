import sys
sys.setrecursionlimit(100000)
si = sys.stdin.readline
n, m = map(int, si().split())

parents = [i for i in range(n + 1)]

def find(u):
    if parents[u] != u:
        parents[u] = find(parents[u])
    return parents[u]

def union(u, v):
    a = find(u)
    b = find(v)
    if a != b:
        parents[b] = a
        
for _ in range(m):
    op, a, b = map(int, si().split())
    if op == 0:
        union(a, b)
    else:
        pa = find(a)
        pb = find(b)
        if pa == pb:
            print("YES")
        else:
            print("NO")