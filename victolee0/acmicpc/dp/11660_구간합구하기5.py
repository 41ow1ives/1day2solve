import sys
si = sys.stdin.readline
n, m = map(int, si().split())
nums = [list(map(int, si().split())) for _ in range(n)]
'''
for _ in range(m):
    x1, y1, x2, y2 = map(int, si().split())
    tmp = nums[x1 - 1:x2]
    cnt = 0
    for i in range(len(tmp)):
        cnt += sum(tmp[i][y1 - 1:y2])
    print(cnt)'''
    
dp = [[0] * (n + 1)  for _ in range(n + 1)]

for j in range(1, n + 1):
    tmp = 0
    for i in range(1, n + 1):
        tmp += nums[j - 1][i - 1]
        dp[j][i] = tmp
        
for _ in range(m):
    x1, y1, x2, y2 = map(int, si().split())
    cnt = 0
    for i in range(x1, x2 + 1):
        cnt += dp[i][y2] - dp[i][y1 - 1]
    print(cnt)
