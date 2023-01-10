from collections import defaultdict


def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report = list(set(report))  # 중복 신고 건 제거

    cnt = defaultdict(int)  # 신고 횟수를 저장할 딕셔너리
    users = defaultdict(set)  # 신고 내용 저장할 딕셔너리

    for r in report:
        u1, u2 = r.split()  # u1: 신고 한 사람, u2 신고 당한 사람
        users[u1].add(u2)  # u1가 신고한 사람들 추가 ##########################
        cnt[u2] += 1  # u2가 신고 당한 횟수 카운트

    i = 0
    for id in id_list:  # 전체 사용자들에 대해서
        for u in users[id]:  # 개별 사용자가 신고한 사람들 중
            if cnt[u] >= k:  # 신고를 k번 이상 받은 사람이 있다면,
                answer[i] += 1
        i += 1

    return answer
