# 제목 : 트리의 부모 찾기
# 분류 : 백트래킹, Silver 2
# 출처 : 백준 11725

import sys
from collections import deque
sys.setrecursionlimit(10**6)

n = int(input())
T = {i+1: [] for i in range(n)}
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    T[a] += [b]
    T[b] += [a]

root = [0] * (n+1)
visited = [False] * (n+1)

def bfs(s):
    visited[s] = True
    q = deque()
    q.append(s)

    while q:
        w = q.popleft()
        for v in T[w]:
            if not visited[v]:
                q.append(v)
                root[v] = w
                visited[v] = True

bfs(1)
print(*root[2:])


root = [0] * (n+1)
visited = [False] * (n+1)

def dfs(s):
    visited[s] = True

    for v in T[s]:
        if not visited[v]:
            root[v] = s
            dfs(v)

dfs(1)
print(*root[2:])