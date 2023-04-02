# 제목 : 징검다리 건너기
# 분류 : DP, Silver 1
# 출처 : 백준 21317

N = int(input())
E = [list(map(int, input().split())) for _ in range(N-1)]
K = int(input())
dp = [0] * N

if N >= 2:
    dp[1] = E[0][0]

if N >= 3:
    for i in range(2, N):
        dp[i] = min(dp[i-1] + E[i-1][0], dp[i-2] + E[i-2][1])

    dp2 = dp.copy()
    for i in range(3, N):
        dp2[i] = min(dp2[i-1] + E[i-1][0], dp2[i-2] + E[i-2][1], dp[i-3] + K)

if N >= 3:
    print(min(dp[N-1], dp2[N-1]))
else:
    print(dp[N-1])