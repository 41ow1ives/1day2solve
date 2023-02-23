# https://www.acmicpc.net/problem/10812
# 바구니 순서 바꾸기
"""
asterisk를 이용해서 리스트의 원소 프린트 하기
"""
n, m = map(int, input().split())
bag = [i for i in range(0, n + 1)]

for _ in range(m):
    i, j, k = map(int, input().split())
    bag[i : j + 1] = bag[k : j + 1] + bag[i:k]
print(*bag[1:])
