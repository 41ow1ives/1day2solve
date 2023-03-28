import sys
sys.setrecursionlimit(100003)
si = sys.stdin.readline
n = int(si())
nums = [0] + list(map(int, si().split()))

con = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, si().split())
    con[u].append(v)
    con[v].append(u)

# 우수 / 일반
dp = [[0, 0] for _ in range(n + 1)]

def dfs(x, par):
    dp[x][0] = nums[x]
    for y in con[x]:
        if y == par: continue
        dfs(y, x)
        dp[x][0] += dp[y][1]
        dp[x][1] += max(dp[y])

dfs(1, -1)
print(max(dp[1]))