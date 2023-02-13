# 제목 : 절댓값 힙
# 분류 : 힙 / Silver 1
# 출처 : 백준 11286

import heapq, sys

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    x = int(sys.stdin.readline())

    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])

    else:
        heapq.heappush(heap, (abs(x), x))