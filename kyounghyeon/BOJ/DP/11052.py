# 제목 : 카드 구매하기
# 분류 : DP , Silver 1
# 출처 : 백준 11052

n = int(input())
p = [0] + list(map(int, input().split()))
dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    m = 0
    for j in range(i):
        m = max(m, p[i-j] + dp[j])
    dp[i] = m

print(dp[n])
