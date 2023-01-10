# 제목 : 일곱 난쟁이
# 분류 : 완전탐색
# 출처 : 백준 2309

from itertools import combinations

height = [int(input()) for _ in range(9)]
all_combi = combinations(height, 7)

for h in all_combi:
    if sum(h) == 100:
        for i in sorted(h):
            print(i)
        break