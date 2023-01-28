# 제목 : N과 M (2)
# 분류 : 백트래킹, Silver 3
# 출처 : 백준 15650

from itertools import combinations
n, m = map(int, input().split())

lst = list(range(1,n+1))
seq = list(combinations(lst, m))

for i in seq:
    for j in i:
        print(j, end = " ")
    print()