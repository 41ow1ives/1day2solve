import sys
import heapq
si = sys.stdin.readline

n = int(si())
m = int(si())
con = [[] for _ in range(n + 1)]
dist = [100000 * 1000] * (n + 1)
for _ in range(m):
    start, end, weight = map(int, si().split())
    con[start].append((end, weight))
start, end = map(int,si().split())
dist[start] = 0

Q = []
heapq.heappush(Q, (0, start))
while Q:
    dist_x, x = heapq.heappop(Q)
    if dist[x] != dist_x:
        continue
    
    for v, w in con[x]:
        if dist[v] > dist[x] + w:
            dist[v] = dist[x] + w
            heapq.heappush(Q, (dist[v], v))

print(dist[end])
