# 제목 : 이중 우선순위 큐
# 분류 : 힙, 우선순위 큐 / Gold 4
# 출처 : 백준 7662

import heapq, sys

t = int(sys.stdin.readline())

for _ in range(t):
    max_heap, min_heap = [], []
    k = int(sys.stdin.readline())
    deleted = [False] * k

    for i in range(k):
        oper, num = sys.stdin.readline().split()
        num = int(num)

        if oper == "I":
            heapq.heappush(min_heap, (num, i))
            heapq.heappush(max_heap, (-num, i))

        else: # oper == "D"

            if num == -1:
                while min_heap and deleted[min_heap[0][1]] == True:
                    heapq.heappop(min_heap)
                if min_heap:
                    deleted[min_heap[0][1]] = True
                    heapq.heappop(min_heap)
            elif num == 1:
                while max_heap and deleted[max_heap[0][1]] == True:
                    heapq.heappop(max_heap)
                if max_heap:
                    deleted[max_heap[0][1]] = True
                    heapq.heappop(max_heap)

    while max_heap and deleted[max_heap[0][1]] == True:
        heapq.heappop(max_heap)
    while min_heap and deleted[min_heap[0][1]] == True:
        heapq.heappop(min_heap)

    if not min_heap:
        print("EMPTY")
    else:
        print(-max_heap[0][0], min_heap[0][0])