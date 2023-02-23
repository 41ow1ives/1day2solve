import sys
si = sys.stdin.readline
n = int(si())

max_dp = [[0, 0, 0] for _ in range(2)]
min_dp = [[999999, 9999999, 999999] for _ in range(2)]
nums = list(map(int, si().split()))
for i in range(3):
    max_dp[0] = nums
    min_dp[0] = nums
    
for i in range(1, n):
    nums = list(map(int, si().split()))
    for j in range(3):
        if j == 0:
            max_dp[1][j] = max(max_dp[0][0], max_dp[0][1]) + nums[j]
            min_dp[1][j] = min(min_dp[0][0], min_dp[0][1]) + nums[j]
        elif j == 1:
            max_dp[1][j] = max(max_dp[0][0], max_dp[0][1], max_dp[0][2]) + nums[j]
            min_dp[1][j] = min(min_dp[0][0], min_dp[0][1], min_dp[0][2]) + nums[j]
        elif j == 2:
            max_dp[1][j] = max(max_dp[0][1], max_dp[0][2]) + nums[j]
            min_dp[1][j] = min(min_dp[0][1], min_dp[0][2]) + nums[j]
    max_dp[0] = max_dp[1][:]
    min_dp[0] = min_dp[1][:]


print(max(max_dp[0]), min(min_dp[0]))
