# 제목 : N과 M (5)
# 분류 : 백트래킹, Silver 3
# 출처 : 백준 15654

from itertools import permutations

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()

seq = permutations(num, m)

for i in seq:
    for j in i:
        print(j, end = " ")
    print()