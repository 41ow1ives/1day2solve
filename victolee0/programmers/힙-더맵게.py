import heapq

def solution(scoville, K):
    
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)
        
    answer = 0
    
    while heap[0] < K:
        now = heapq.heappop(heap) + heapq.heappop(heap) * 2
        heapq.heappush(heap, now)
        answer += 1
        if len(heap) == 1 and heap[0] < K:
            answer = -1
            break
    return answer