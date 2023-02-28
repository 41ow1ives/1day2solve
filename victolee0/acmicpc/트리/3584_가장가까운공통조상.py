import sys

si = sys.stdin.readline
t = int(si())
for _ in range(t):
    n = int(si())
    con = [[] for _ in range(n + 1)]
    parent = [0] * (n + 1)
    for _ in range(n - 1):
        a, b = map(int, si().split())
        parent[b] = a
    
    x, y = map(int, si().split())
    parent_xy = [[0, 0] for _ in range(n + 1)]
    
    dist = 1
    tx = x
    ty = y
    while True:
        px = parent[tx]
        py = parent[ty]
        parent_xy[px][0] = dist
        parent_xy[py][1] = dist
        lst = []
        if px == y:
            lst.append([px, 0])
            break
        if py == x:
            lst.append([py, 0])
        if parent_xy[px][0] * parent_xy[px][1] != 0:
            lst.append((px, min(parent_xy[px])))
        if parent_xy[py][0] * parent_xy[py][1] != 0:
            lst.append((py, min(parent_xy[py])))
        if lst:
            break
        dist += 1
        tx = px
        ty = py
    lst = sorted(lst, key=lambda x:x[1])
    print(lst[0][0])