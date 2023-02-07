# 제목 : 평범한 배낭
# 분류 : DP / Gold 5
# 출처 : 백준 12865

n, k = map(int, input().split())
bag = [list(map(int,input().split())) for _ in range(n)]

cache = [[0]*(k+1) for _ in range(n)]

for i in range(bag[0][0], k+1):
    cache[0][i] = bag[0][1]

for i in range(1, n):
    for j in range(1, k+1):
        if bag[i][0] > j:
            cache[i][j] = cache[i-1][j]
        else:
            cache[i][j] = max(cache[i-1][j], bag[i][1] + cache[i-1][j - bag[i][0]])

print(cache[-1][-1])
