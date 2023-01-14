# 제목 : 1,2,3 더하기
# 분류 : DP, Silver 3
# 출처 : 백준 9095

t = int(input())
num_lst = [int(input()) for _ in range(t)]

n = max(num_lst)
def q(n):

    dp = [0] * (n+1)
    for i in range(n+1):
        if 1<= i <= 3:
            dp[i] = 2**(i-1)
        else:
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return dp

dp = q(n)
for num in num_lst:
    print(dp[num])