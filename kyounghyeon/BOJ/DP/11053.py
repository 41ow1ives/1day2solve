# 제목 : 가장 긴 증가하는 부분 수열
# 분류 : DP, Silver 2
# 출처 : 백준 11053

n = int(input())
seq = list(map(int, input().split()))
dp = [1] * n
m = seq[0]

for i in range(n):
    for j in range(i):
        if seq[i] > seq[j]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp))