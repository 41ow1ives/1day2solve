import sys
si = sys.stdin.readline
n = int(si())
nums = list(map(int, si().split()))

dp = [[0] * 21 for _ in range(n)]

dp[0][nums[0]] = 1

for i in range(1, n - 1):
    for prev in range(21):
        for cur in [prev - nums[i], prev + nums[i]]:
            if 0 <= cur <= 20:
                dp[i][cur] += dp[i - 1][prev]
                
print(dp[n - 2][nums[n - 1]])
        