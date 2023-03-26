# 제목 : 랜선 자르기
# 분류 : 이분탐색, Silver 2
# 출처 : 백준 1654

import sys
input = sys.stdin.readline

K, N = map(int, input().split())
code = [int(input()) for _ in range(K)]

low = 1
high = max(code)

while low <= high:

    mid = (low + high) // 2
    cnt = sum(map(lambda x: x // mid, code))

    if cnt < N:
        high = mid - 1
    else:
        low = mid + 1

print(high)
