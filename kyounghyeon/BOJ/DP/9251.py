# 제목 : LCS
# 분류 : DP, Gold 5
# 출처 : 백준 9251

seq1 = ' ' + input()
seq2 = ' ' + input()
n1, n2 = len(seq1), len(seq2)

dp = [[0] * n2 for _ in range(n1)]

for i in range(1, n1):
    for j in range(1, n2):
        if seq1[i] == seq2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])

