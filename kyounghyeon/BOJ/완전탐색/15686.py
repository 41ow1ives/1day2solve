# 제목 : 치킨 배달
# 분류 : 완전탐색/백트래킹 , Gold 5
# 출처 : 백준 15686

import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(n)]
house, chicken = [], []

for i in range(n):
    for j in range(n):
        if G[i][j] == 1:
            house.append((i, j))
        elif G[i][j] == 2:
            chicken.append((i, j))

chicken_dist = []
for combi in combinations(chicken, m):
    dist = 0
    for i, j in house:
        dist += min(map(lambda x: abs(x[0]-i) + abs(x[1]-j), combi))
    chicken_dist.append(dist)

print(min(chicken_dist))