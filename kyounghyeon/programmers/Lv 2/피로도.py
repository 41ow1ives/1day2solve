from itertools import permutations

def solution(k, dungeons):
    n = len(dungeons)
    cases = list(permutations(list(range(0, n)), n))
    total = []

    for case in cases:
        cnt = 0
        p = k
        for i in case:
            if p >= dungeons[i][0]:
                p -= dungeons[i][1]
                cnt += 1
        total.append(cnt)

    answer = max(total)
    return answer