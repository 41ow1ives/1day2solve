import sys
si = sys.stdin.readline
t = int(si())
MOD = 1000000009
dp = [[0, 0, 0, 0] for _ in range(100001)]

dp[1] = [0, 1, 0, 0]
dp[2] = [0, 0, 1, 0]
dp[3] = [0, 1, 1, 1]

for i in range(4, 100001):
    dp[i][1] = (sum(dp[i - 1]) - dp[i - 1][1]) % MOD
    dp[i][2] = (sum(dp[i - 2]) - dp[i - 2][2]) % MOD
    dp[i][3] = (sum(dp[i - 3]) - dp[i - 3][3]) % MOD

for _ in range(t):
    n = int(si())
    print(sum(dp[n]) % MOD)