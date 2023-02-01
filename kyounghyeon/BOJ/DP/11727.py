# 제목 : 2xn 타일링 2
# 분류 : DP, Silver 3
# 출처 : 백준 11727

n = int(input())
dp = [0] * 1001

# 초기값 지정
dp[0] = 1
dp[1] = 1

for i in range(2, n+1):
    dp[i] = dp[i-1] + 2 * dp[i-2]

print(dp[n]%10007)

