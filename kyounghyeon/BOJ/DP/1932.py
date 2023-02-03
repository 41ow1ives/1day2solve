# 제목 : 정수 삼각형
# 분류 : DP, Silver 1
# 출처 : 백준 1932

n = int(input())
tri = []
dp =[[] for _ in range(n)]

for i in range(n):
    tri.append(list(map(int, input().split())))
dp[0].append(tri[0][0])

for i in range(1,n):
    for j in range(i+1):
        if j == 0: # 왼쪽으로만
            dp[i].append(dp[i-1][j] + tri[i][j])
        elif i == j: # 오른쪽으로만
            dp[i].append(dp[i-1][j-1] + tri[i][j])
        else:
            dp[i].append(max(dp[i-1][j-1], dp[i-1][j]) + tri[i][j])

print(max(dp[-1]))