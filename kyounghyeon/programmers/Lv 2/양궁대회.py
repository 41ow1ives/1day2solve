# 2022 카카오 블라인드 채용
# 완전탐색

from itertools import combinations_with_replacement

def solution(n, info):

    result_lst = []

    for combi in combinations_with_replacement(range(11), n):

        info2 = [0] * 11
        ryan = 0
        apeach = 0

        for score in combi:
            info2[10-score] += 1

        for i in range(11):
            if info[i] == 0 and info2[i] == 0:
                continue
            elif info[i] >= info2[i]:
                apeach += 10-i
            elif info[i] < info2[i]:
                ryan += 10-i

        if ryan > apeach:
            result_lst.append([ryan-apeach, info2])

    if len(result_lst) == 0:
        return [-1]
    else:
        return max(result_lst, key = lambda x: (x[0]))[1]

'''
# 백트래킹으로 구현한 코드 -> 답은 구하는데 시간 초과
def solution(n, info):
    target = [0] * 11
    result_lst = []

    def _win(target):
        apeach, ryan = 0, 0
        for i in range(11):
            if info[i] != 0 or target[i] != 0:
                if info[i] >= target[i]:
                    apeach += 10 - i
                else:
                    ryan += 10 - i

        if apeach >= ryan:
            return False, abs(apeach - ryan)
        else:
            return True, abs(apeach - ryan)

    def dfs():
        if sum(target) == n:
            win, diff = _win(target)
            if win:
                result_lst.append([diff, target.copy()])
            return

        for i in range(11):
            if target[i] == info[i] + 1:
                continue
            target[i] += 1
            dfs()
            target[i] -= 1

    dfs()
    if not result_lst:
        return [-1]
    else:
        max_diff = max(result_lst, key=lambda x: (x[0], x[1][::-1]))
        answer = max_diff[1]
        return answer
'''