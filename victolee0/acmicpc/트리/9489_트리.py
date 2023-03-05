import sys
from collections import deque
si = sys.stdin.readline
while True:
    n, k = map(int, si().split())
    if n == 0 and k == 0:
        break
    nums = list(map(int, si().split()))
    parent = [-1] * (1000001)
    Q = deque()
    for i, x in enumerate(nums):
        if i == 0:
            parent[x] = 0
            prev = x
            Q.append(x)
            continue

        if prev + 1 != x:
            p = Q.popleft()
            
        parent[x] = p
        prev = x
        Q.append(x)
    
    ans = 0
    for x in nums:
        if parent[parent[x]] == parent[parent[k]] and parent[x] != parent[k]:
            ans += 1

    print(ans)