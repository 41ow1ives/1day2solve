# 제목 : 최단 경로
# 분류 : 다익스트라 / 그래프 , Gold 4
# 출처 : 백준 1753

import sys, heapq

INF = int(1e9)
input = sys.stdin.readline
v, e = map(int, input().split())
k = int(input())
G = {i : [] for i in range(1, v+1)}

for _ in range(e):
    a, b, w = map(int, input().split())
    G[a].append((b, w))

dist = [INF] * (v+1)

def dijkstra(start):

    h = []
    heapq.heappush(h, (0, start))
    dist[start] = 0

    while h:
        d, now = heapq.heappop(h)
        if dist[now] < d: # 현재 노드가 이미 갱신되었고, 현재 거리보다 작다면
            continue
        for node in G[now]:
            cost = d + node[1]
            if cost < dist[node[0]]:
                dist[node[0]] = cost
                heapq.heappush(h, (cost, node[0]))

dijkstra(k)
for i in range(1, v+1):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i])