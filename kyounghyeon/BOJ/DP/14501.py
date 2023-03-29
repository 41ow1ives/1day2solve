# 제목 : 퇴사
# 분류 : DP/완탐, Silver 3
# 출처 : 백준 14501

N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (N+1)

for i in range(N):
    for j in range(i + lst[i][0], N+1):
        if dp[j] < dp[i] + lst[i][1]:
            dp[j] = dp[i] + lst[i][1]

print(dp[-1])