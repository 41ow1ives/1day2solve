'''
효율성 통과를 위한 idea
1) key값을 통해 빠른 접근이 가능한 hashmap(딕셔너리)을 사용하여 조건 찾고,
2) 시간복잡도가 낮은 이분탐색 사용하여 점수 비교
'''
from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    info = list(map(lambda x: list(x.split()), info))
    query = list(map(lambda x: list(x.replace(" and", "").split()), query))
    all_cond_dict = {}
    answer = []

    # 가능한 info 조합 모두 생성
    for user in info:
        cond = user[:-1]  # 언어, 직무, 경력, 음식
        score = int(user[-1])  # 코테 점수

        # 조건은 총 4개, 각각 있거나 없거나(-) 한 경우 => 총 2^4 = 16개
        for i in range(5):
            for c in combinations(cond, i):  # 0개~4개 선택하는 조합 모두 구하면 16개
                c = ''.join(c)
                if c in all_cond_dict:
                    all_cond_dict[c] += [score]
                else:
                    all_cond_dict[c] = [score]

    # score 오름차순 정리
    for d in all_cond_dict:
        all_cond_dict[d].sort()

    # 쿼리별로 조건에 맞는 유저 찾기
    for q in query:
        q_cond = ''.join(q[:-1]).replace('-', '')
        q_score = int(q[-1])

        # q_cond가 존재하지 않는 경우에 대처하기 위해 try/except 사용 (if 써도 됨)
        try:
            idx = bisect_left(all_cond_dict[q_cond], q_score)
            answer.append(len(all_cond_dict[q_cond]) - idx)
        except:
            answer.append(0)

    return answer

''' 효율성 개나줘버린 첫 코드..
def solution(info, query):
    query = list(map(lambda x: list(x.replace(' and', "").split()), query))
    info = list(map(lambda x: list(x.split()), info))

    answer = []

    for lang, job, year, food, score in query:
        print(lang, job, year, food, score)
        cnt = 0
        for user in info:
            if lang == user[0] or lang == "-":
                if job == user[1] or job == "-":
                    if year == user[2] or year == "-":
                        if food == user[3] or food == "-":
                            if int(score) <= int(user[4]):
                                cnt += 1

        answer.append(cnt)

    return answer
'''


















'''
query = list(map(lambda x: list(x.replace(' and', "").split()), query))
info = list(map(lambda x: list(x.split()), info))

answer = []

for lang, job, year, food, score in query:
    print(lang, job, year, food, score)
    cnt = 0
    for user in info:
        if lang == user[0] or lang == "-":
            if job == user[1] or job == "-":
                if year == user[2] or year == "-":
                    if food == user[3] or food == "-":
                        if int(score) <= int(user[4]):
                            cnt += 1

    answer.append(cnt)
'''




