# 제목 : 파티
# 분류 : 다익스트라 / 그래프 , Gold 3
# 출처 : 백준 1238

import sys, heapq
input = sys.stdin.readline

INF = int(1e9)
N, M, X = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(1, M+1):
    v, w, k = map(int, input().split())
    G[v].append((w, k))

def find(s, dist):
    h = []
    heapq.heappush(h, (0, s))
    dist[s] = 0

    while h:
        d, e = heapq.heappop(h)
        if dist[e] < d:
            continue

        for node in G[e]:
            if d + node[1] < dist[node[0]]:
                dist[node[0]] = d + node[1]
                heapq.heappush(h, (dist[node[0]], node[0]))

    return dist

dist = [[INF] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    dist[i] = find(i, dist[i])

for j in range(1, N+1):
    dist[X][j] += dist[j][X]

print(max(dist[X][1:]))