import sys

si = sys.stdin.readline
n = int(input())

adj_mat = {i + 1: [] for i in range(n)}
for i in range(n - 1):
    a, b = map(int, si().split())
    adj_mat[a] += [b]
    adj_mat[b] += [a]

visited = [0 for _ in range(n + 1)]
parent = [0 for _ in range(n + 1)]
queue = [1]
while queue:
    now = queue.pop(0)
    if visited[now]:
        continue
    visited[now] = 1
    queue += adj_mat[now]
    for i in adj_mat[now]:
        if parent[i]:
            continue
        parent[i] = now

for i in parent[2:]:
    print(i)