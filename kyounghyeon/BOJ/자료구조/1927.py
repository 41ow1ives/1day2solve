# 제목 : 최소 힙
# 분류 : 힙, Silver 2
# 출처 : 백준 2606

import heapq, sys

n = int(input())
heap = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)
    elif x == int(x):
        heapq.heappush(heap, x)
