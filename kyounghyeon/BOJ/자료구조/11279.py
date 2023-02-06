# 제목 : 최대 힙
# 분류 : 힙 / Silver 2
# 출처 : 백준 11279

import heapq, sys

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-1 * heapq.heappop(heap))
    else:
        heapq.heappush(heap, -num)
