# 제목 : 1로 만들기
# 분류 : DP, Silver 3
# 출처 : 백준 1463


n = int(input())
dp = [0] * (n+1)

for i in range(2, n+1):
    lst = []
    if i % 2 == 0: lst.append(dp[i // 2] + 1)
    if i % 3 == 0: lst.append(dp[i // 3] + 1)
    lst.append(dp[i - 1] + 1)

    dp[i] = min(lst)

print(dp[n])