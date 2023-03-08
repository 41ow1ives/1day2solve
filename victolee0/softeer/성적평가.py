import sys
import heapq
si = sys.stdin.readline
n = int(si())


total_score = [0] * n
for _ in range(3):
    score_map = [[] for _ in range(1001)]
    test = list(map(int, si().split()))
    for i, x in enumerate(zip(total_score, test)):
        total_score[i] = sum(x)

    heap = []
    for i, x in enumerate(test):
        heapq.heappush(heap, x)
        score_map[x].append(i)
    
    tmp_rank = [0] * n
    while heap:
        x = heapq.heappop(heap)
        if not score_map[x]:
            continue
        p = score_map[x].pop()
        now_rank = len(heap) + 1
        tmp_rank[p] = now_rank
        
        if score_map[x]:
            now_rank = now_rank - len(score_map[x])
            tmp_rank[p] = now_rank
            for y in score_map[x]:
                tmp_rank[y] = now_rank

            score_map[x] = []
    print(' '.join([str(x) for x in tmp_rank]))

rank = [0] * n
heap = total_score[:]
heapq.heapify(heap)
score_map = {x: 0 for x in total_score}
while heap:
    x = heapq.heappop(heap)
    if score_map[x]:
        score_map[x] -= 1
    else:
        score_map[x] = len(heap) + 1

    
for i, x in enumerate(total_score):
    rank[i] = score_map[x]

print(' '.join([str(x) for x in rank]))