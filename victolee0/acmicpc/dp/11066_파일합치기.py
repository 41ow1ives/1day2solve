import sys
si = sys.stdin.readline
t = int(si())
for _ in range(t):
    k = int(si())
    sizes = list(map(int, si().split()))
    dp = [[0] * k for __ in range(k)]
    sum_of_size = [[0] * k for __ in range(k)]
    for i in range(k):
        for j in range(k):
            if i == j:
                sum_of_size[i][j] = sizes[j]
            else:
                sum_of_size[i][j] = sum_of_size[i][j-1] + sizes[j]
    # 0,0 1,1 2,2 3,3, 0,1 1,2 2,3 
    for len in range(k):
        for i in range(k - len):
            j = i + len
            if i == j:
                continue
            if j == i:
                dp[i][j] = sizes[i]
            else:
                for p in range(i, j):
                    if dp[i][j] == 0:                    
                        dp[i][j] = dp[i][p] + dp[p + 1][j] + sum_of_size[i][j]
                    else:
                        dp[i][j] = min(dp[i][j], dp[i][p] + dp[p + 1][j] + sum_of_size[i][j])
    
    print(dp[0][k - 1])