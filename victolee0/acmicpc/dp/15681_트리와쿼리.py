import sys
sys.setrecursionlimit(100001)
si = sys.stdin.readline
n, r, q = map(int, si().split())

con = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, si().split())
    con[u].append(v)
    con[v].append(u)
    
dp = [0] * (n + 1)

def dfs(now, prev):
    dp[now] = 1
    for x in con[now]:
        if x == prev:
            continue
        dfs(x, now)
        dp[now] += dp[x]
        
dfs(r, -1)

for _ in range(q):
    u = int(si())
    print(dp[u])
