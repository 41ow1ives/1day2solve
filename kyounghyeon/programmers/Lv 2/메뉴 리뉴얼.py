# 2021 KAKAO BLIND RECRUITING

from collections import Counter
from itertools import combinations

def solution(orders, course):
    answer = []
    for c in course:
        lst = []
        for o in orders:
            case = list(combinations(sorted(o), c))
            for combi in case:
                lst.append(combi)
        cnt = Counter(lst)
        if cnt and max(cnt.values()) >= 2:
            answer += [''.join(i) for i in cnt.keys() if cnt[i] == max(cnt.values())]

    return sorted(answer)

