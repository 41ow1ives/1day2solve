# 제목 : 계단 오르기
# 분류 : DP, Silver 3
# 출처 : 백준 2579

n = int(input())
stair = [int(input()) for _ in range(n)]

dp = [0] * n
for i in range(n):
    if i == 0:
        dp[i] = stair[i]
    elif i == 1:
        dp[i] = stair[i] + dp[i-1]
    elif i == 2:
        dp[i] = stair[i] + max(stair[i-1], stair[i-2])
    else:
        dp[i] = stair[i] + max(stair[i-1] + dp[i-3], dp[i-2])

print(dp[n-1])

