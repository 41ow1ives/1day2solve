n = int(input())
# 4
# 3 7(3 + 4) 17(7 + 10) 41(17 + 24)
dp = [1, 3]
for i in range(2, n + 1):
    dp.append((dp[i - 1] * 2 + dp[i - 2]) % 9901)
    
print(dp[n])