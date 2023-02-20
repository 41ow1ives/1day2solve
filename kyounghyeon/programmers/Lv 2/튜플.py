# 프로그래머스 2019 카카오 개발자 겨울 인턴십

def solution(s):
    s = list(map(lambda x: list(map(int, x.split(","))), s.strip("{}").split("},{")))
    s.sort(key=lambda x: len(x))

    answer = []
    answer.append(s[0][0])

    for i in s[1:]:
        for j in i:
            if j not in answer:
                answer.append(j)

    return answer