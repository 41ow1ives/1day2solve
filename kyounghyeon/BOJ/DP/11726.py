# 제목 : 2xn 타일링
# 분류 : DP
# 출처 : 백준 11726


n = int(input())
cache = [0]*1001
cache[1] = 1
cache[2] = 2

for i in range(3, 1001):
    cache[i] = cache[i-1] + cache[i-2]

print(cache[n] % 10007)

