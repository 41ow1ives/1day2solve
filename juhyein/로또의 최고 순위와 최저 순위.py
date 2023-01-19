from collections import Counter

def solution(lottos, win_nums):
    worst = len(list(set(lottos) & set(win_nums)))
    count = Counter(lottos)
    best = count[0] + worst
    
    # best = 0, worst = 0 인 경우 주의
    return [min(6,(6-best+1)), min(6, (6-worst+1))]

# 참고
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]
