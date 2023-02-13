# 제목 : 구간 합 구하기 5
# 분류 : DP / Silver 1
# 출처 : 백준 11660

import sys

n, m = map(int, sys.stdin.readline().split())
table = []
dp = [[0] * (n+1) for _ in range(n+1)]

for _ in range(n):
    table.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n+1):
    for j in range(1, n+1):
        dp[i][j] = table[i-1][j-1] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1])

