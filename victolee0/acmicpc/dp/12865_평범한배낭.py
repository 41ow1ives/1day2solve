import sys

si = sys.stdin.readline
n, k = map(int, si().split())
lst = []
dp = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(n):
    w, v = map(int, si().split())
    lst += [[w, v]]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        if lst[i - 1][0] > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i-1][j - lst[i - 1][0]] + lst[i - 1][1])

print(dp[n][k])