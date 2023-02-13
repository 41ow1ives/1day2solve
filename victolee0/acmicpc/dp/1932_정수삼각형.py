import sys
si = sys.stdin.readline

n = int(si())
triangle = []
dp = []
for _ in range(n):
    tmp_input = list(map(int, si().split()))
    triangle.append(tmp_input)
    tmp_dp = [0] * len(tmp_input)
    dp.append(tmp_dp)

dp[0][0] = triangle[0][0]
for i in range(1, n):
    for j, val in enumerate(triangle[i]):
        if j == 0:
            dp[i][j] = dp[i - 1][j] + val
            continue
        if j == len(triangle[i]) - 1:
            dp[i][j] = dp[i - 1][j - 1] + val
            continue
        dp[i][j] = max(dp[i - 1][j] + val, dp[i - 1][j - 1] + val)
        
print(max(dp[n - 1]))