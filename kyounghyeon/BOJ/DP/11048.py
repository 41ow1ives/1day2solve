# 제목 : 이동하기
# 분류 : DP, Silver 2
# 출처 : 백준 11048

n, m = map(int, input().split())
maze = [[0] * (m+1) for _ in range(n+1)]
dp = [[0] * (m+1) for _ in range(n+1)]


for i in range(1, n+1):
    maze[i] = [0] + list(map(int, input().split()))

for i in range(1, n+1):
    for j in range(1, m+1):
        if i == 1:
            dp[i][j] = dp[i][j-1] + maze[i][j]

        elif j == 1:
            dp[i][j] = dp[i-1][j] + maze[i][j]

        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + maze[i][j]

print(dp[-1][-1])