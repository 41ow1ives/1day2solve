import sys
si = sys.stdin.readline
n = int(si())
p = [0] + list(map(int, si().split()))

dp = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i - j] + p[j])
    
print(dp[n])