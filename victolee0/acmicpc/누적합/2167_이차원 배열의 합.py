import sys
si = sys.stdin.readline
n, m = map(int, si().split())
nums = []
for _ in range(n):
    nums.append(list(map(int, si().split())))
ans = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        ans[i][j] = ans[i][j-1] + nums[i-1][j-1]

k = int(si())
for _ in range(k):
    i, j, x, y = map(int, si().split())
    res = 0
    for t in range(i, x + 1):
        res += ans[t][y] - ans[t][j-1]
    print(res)