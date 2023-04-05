import sys
si = sys.stdin.readline
n = int(si())
m = int(si())
INF = n * 100001
cost = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    cost[i][i] = 0
            
            
for _ in range(m):
    a, b, c = map(int, si().split())
    cost[a][b] = min(cost[a][b], c)
        
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            cost[a][b] = min(cost[a][b], cost[a][k] + cost[k][b])

for i in range(1, n + 1):
    out = ' '.join([str(a) for a in cost[i][1:]])
    out = out.replace(str(INF), '0')
    print(out)
    