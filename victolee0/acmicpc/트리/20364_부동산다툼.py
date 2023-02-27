import sys
from collections import deque
si = sys.stdin.readline
n, q = map(int, si().split())

owned = [0] * (n + 1)
for _ in range(q):
    x = int(si())
    y = x
    res = 0
    possible = True
    while x:
        if owned[x]:
            res = x
            possible = False
        x = x // 2
    if possible:
        owned[y] = 1
    print(res)
