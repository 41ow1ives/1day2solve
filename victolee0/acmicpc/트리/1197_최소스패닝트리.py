import sys
import heapq

si = sys.stdin.readline
v, e = map(int, si().split())

graph = {
    i + 1: [] for i in range(v)
}
for _ in range(e):
    a, b, c = map(int, si().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
   

tree = [(0, 1)]
ans = 0
cnt = 0
visited = [0] * (v + 1)
while cnt < v:
    weight, node = heapq.heappop(tree)
    if visited[node]:
        continue
    visited[node] = 1
    ans += weight
    cnt += 1
    for x, w in graph[node]:
        heapq.heappush(tree, (w, x))

print(ans)
