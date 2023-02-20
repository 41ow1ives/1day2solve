n = int(input())

dp = [0] * 5001
dp[3] = 1
dp[5] = 1

for i in range(6, 5001):
    if dp[i - 3] != 0 and dp[i - 5] == 0:
        dp[i] = dp[i - 3] + 1
        
    elif dp[i - 3] == 0 and dp[i - 5] != 0:
        dp[i] = dp[i - 5] + 1
        
    elif dp[i - 3] != 0 and dp[i - 5] != 0:
        dp[i] = min(dp[i - 3], dp[i - 5]) + 1        

    
if dp[n] == 0:
    print(-1)
else:
    print(dp[n])