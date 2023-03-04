# 제목 : 최소 스패닝 트리
# 분류 : 그래프 / MST , Gold 4
# 출처 : 백준 1197

'''
- 신장 트리 : 주어진 그래프 G의 트리가 되는 부분 연결 그래프
- 최소 신장 트리 : 하나의 연결성분으로 이루어진 무방향 가중치 그래프에서
                 간선들의 가중치의 합이 최소가되는 부분 그래프
'''

import sys
input = sys.stdin.readline
v, e = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(e)]

'''
Kruskal / 간선 기준
간선의 가중치가 가장 작은 것부터 추가할 수 있는지 없는지 판단하여 추가/패스 결정 (find, union)
'''

G.sort(key = lambda x: x[2]) # 가중치 기준 오름차순 정렬

def find(u): # 정점의 부모 찾기
    if u != parent[u]:
        parent[u] = find(parent[u])
    return parent[u]

def union(u, v):
    root1 = find(u)
    root2 = find(v)
    parent[root2] = root1

parent = []
for i in range(v+1):
    parent.append(i)

mst = []
mst_edges = 0
mst_cost = 0
while True:
    if mst_edges == v-1:
        break
    a, b, wt = G.pop(0)
    if find(a) != find(b):
        union(a, b)
        mst.append((a, b))
        mst_cost += wt
        mst_edges += 1

print(mst_cost)

'''
Prim / 정점 기준
임의의 정점을 시작점으로 해서 연결된 정점에서 갈 수 있는 모든 정점 중 가중치가 가장 작은 정점을 MST에 추가
'''

import sys
input = sys.stdin.readline

v, e = map(int, input().split())
G = [[] for _ in range(v+1)]

for _ in range(v+1):
    a, b, w = map(int, input().split())
    G[a].append([b, w])
    G[b].append([a, w])

visited = [False for _ in range(v+1)]
dist = [sys.maxsize for _ in range(v+1)]
dist[1] = 0

''' # 이전 정점 (연결된 정점 알기 위한 리스트)
prev = [None for _ in range(v)]
prev[1] = 1
'''

for _ in range(1, v+1):
    u = -1
    min_dist = sys.maxsize
    for i in range(1, v+1):
        if not visited[i] and dist[i] < min_dist:
            min_dist = dist[i]
            u = i
    visited[u] = True # 맨 처음은 정점 1
    for b, wt in G[u]: # 정점 1에 연결된 정점들에 대해,
        if not visited[b]:
            if wt < dist[b]: # 방문도 안했고, 해당 정점의 도달할 수 있는 거리가 더 짧아지면
                dist[b] = wt

mst_cost = sum(dist[1:])
print(mst_cost)

