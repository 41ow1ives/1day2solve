import sys
import heapq
si = sys.stdin.readline

t = int(si())
for _ in range(t):
    k = int(si())
    max_Q = []
    min_Q = []
    visited = [False] * 1000001
    for i in range(k):
        op, x = si().split()
        x = int(x)
        if op == 'I':
            heapq.heappush(max_Q, (-x, i))
            heapq.heappush(min_Q, (x, i))
            visited[i] = True
            continue
        if op == 'D':
            if x == 1:
                while max_Q and not visited[max_Q[0][1]]:
                    heapq.heappop(max_Q)

                if max_Q:
                    visited[max_Q[0][1]] = False
                    heapq.heappop(max_Q)
            else:
                while min_Q and not visited[min_Q[0][1]]:
                    heapq.heappop(min_Q)
                if min_Q:
                    visited[min_Q[0][1]] = False
                    heapq.heappop(min_Q)
    
    while max_Q and not visited[max_Q[0][1]]:
        heapq.heappop(max_Q)
    
    while min_Q and not visited[min_Q[0][1]]:
        heapq.heappop(min_Q)

    if not max_Q or not min_Q:
        print("EMPTY")
    else:
        print(-max_Q[0][0], min_Q[0][0])