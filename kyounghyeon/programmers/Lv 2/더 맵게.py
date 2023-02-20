# 제목 : 더 맵게
# 분류 : 힙(Heap), Lv 2
# 출처 : 프로그래머스

import heapq

def solution(scoville, K):
    answer = 0
    for s in scoville:
        heapq.heapify(scoville)
        first = heapq.heappop(scoville)

        while first < K:
            if len(scoville) == 0:
                return -1
            second = heapq.heappop(scoville)
            heapq.heappush(scoville, 2 * second + first)
            first = heapq.heappop(scoville)
            answer += 1

    return answer