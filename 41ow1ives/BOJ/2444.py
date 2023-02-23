# https://www.acmicpc.net/problem/2444
# 별 찍기 - 7]
"""
단순 구현 문제
두개를 print할 때 ,로 연결하면 sep=" "가 적용되기 때문에 +로 연결해야 한다.
"""


n = int(input())

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
