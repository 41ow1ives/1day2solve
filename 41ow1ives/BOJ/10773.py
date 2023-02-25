# https://www.acmicpc.net/problem/10773
# 제로

import sys

k = int(sys.stdin.readline())

answer = []

for _ in range(k):
    n = int(sys.stdin.readline())
    if n == 0:
        answer.pop()
    else:
        answer.append(n)
print(sum(answer))
