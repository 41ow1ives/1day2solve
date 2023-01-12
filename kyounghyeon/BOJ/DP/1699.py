# 제목 : 제곱수의 합
# 분류 : DP, Silver 2
# 출처 : 백준 1699

import math
n = int(input())
dp = [i for i in range(n+1)]

for i in range(1, n+1):
    k = int(math.sqrt(i))
    for j in range(1, k+1):
        if dp[i] > dp[i-j**2] + 1:
            dp[i] = dp[i-j**2] + 1

print(dp[n])



