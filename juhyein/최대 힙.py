import heapq
from sys import stdin


n = int(stdin.readline())
heap = list()

for _ in range(n):
    input_num = int(stdin.readline())
    if input_num == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap, [-input_num, input_num])
