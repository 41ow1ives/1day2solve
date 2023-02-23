# https://www.acmicpc.net/problem/3003
# 킹, 퀸, 룩, 비숍, 나이트, 폰

rule = [1, 1, 2, 2, 2, 8]
chess = list(map(int, input().split()))

for r, c in zip(rule, chess):
    print(r-c, end=' ')
