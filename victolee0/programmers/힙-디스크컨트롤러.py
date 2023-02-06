import heapq

def solution(jobs):
    ans = []
    n_jobs = len(jobs)
    tmp = []
    for x, y in jobs:
        heapq.heappush(tmp, (x, y))
    jobs = tmp
    Q = []
    
    while jobs:
        i_t, w_t = heapq.heappop(jobs)
        heapq.heappush(Q, (w_t, i_t))
        now_t = i_t
        while Q:
            w_t, i_t = heapq.heappop(Q)
            now_t += w_t
            ans.append(now_t - i_t)
            while jobs:
                i_t, w_t = heapq.heappop(jobs)
                if i_t > now_t:
                    heapq.heappush(jobs, (i_t, w_t))
                    break
                else:
                    heapq.heappush(Q, (w_t, i_t))

        
    return sum(ans) // n_jobs