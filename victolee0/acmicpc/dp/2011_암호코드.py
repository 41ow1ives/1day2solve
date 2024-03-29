# 25114
# 1 / 2 (2/5, 25) / 3 - 1(2/5/1, 25/1, 2/51) /  (2/5/1/1, 25/11, 25/1/1, 2/51/1, 2/5/11)
# 2222
#2 / (2,2 / 22) / (2,22 / 22,2 / 2,2,2) / (2,2,2,2 / 2,22,2/ 22,2,2/22,22/2,2,22)

pwd = input()

dp = [0] * len(pwd)

if pwd[0] != '0':
    dp[0] = 1
    
for i in range(1, len(pwd)):
    if pwd[i] != '0':
        dp[i] = dp[i - 1]
    if 10 <= int(pwd[i - 1: i + 1]) <= 26:
        if i == 1:
            dp[i] += 1
        else:
            dp[i] += dp[i -2]
        
        dp[i] %= 1000000

print(dp[len(pwd) - 1])