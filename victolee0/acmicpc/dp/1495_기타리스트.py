import sys
si = sys.stdin.readline
n, s, m = map(int, si().split())
v = list(map(int, si().split()))

dp = [[0] * (m + 1) for _ in range(n)]
for cur in [s + v[0], s - v[0]]:
    if cur < 0 or cur > m:
        continue
    dp[0][cur] = 1

for i in range(1, n):
    for prev in range(0, m + 1):
        if dp[i - 1][prev]:
            for cur in [prev - v[i], prev + v[i]]:
                if cur < 0 or cur > m:
                    continue
                dp[i][cur] = 1

flag = True
for i in range(m, -1, -1):
    if dp[n - 1][i]:
        print(i)
        flag = False
        break

if flag:
    print(-1)
