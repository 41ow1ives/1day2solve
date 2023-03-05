# 제목 : 동전 1
# 분류 : DP, Gold 5
# 출처 : 백준 2293

n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]

dp = [0] * (k+1)
dp[0] = 1

for c in coin:
    for i in range(c, k+1):
        dp[i] += dp[i - c]

print(dp[k])