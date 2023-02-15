import sys
si = sys.stdin.readline

dp = [[0 for _ in range(10)] for _ in range(65)]
for i in range(10):
    dp[1][i] = 1
    
for i in range(2, 65):
    for num in range(10):
        for prev in range(10 - num):
            dp[i][num] += dp[i - 1][9 - prev]

t = int(si())
for _ in range(t):
    n = int(si())
    print(sum(dp[n]))
