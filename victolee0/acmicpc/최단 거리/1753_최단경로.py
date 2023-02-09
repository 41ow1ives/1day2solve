import heapq
import sys
si = sys.stdin.readline
V, E = map(int, si().split())
k = int(si())

dist = [11 * 300000] * (V + 1)
dist[k] = 0

con = [[] for _ in range(V + 1)]
for i in range(E):
    u, v, w = map(int, si().split())
    con[u].append((v, w))
    

queue = []
heapq.heappush(queue, (0, k))

while queue:
    dist_x, x = heapq.heappop(queue)
    
    if dist[x] != dist_x:
        continue
    
    for v, w in con[x]:
        if dist[v] > dist[x] + w:
            dist[v] = dist[x] + w
            heapq.heappush(queue, (dist[v], v))

for i in range(1, V + 1):
    if dist[i] == 11 * 300000:
        print("INF")
    else:
        print(dist[i])