# 제목 : 명예의 전당 (1)
# 분류 : ?, Lv 1
# 출처 : 프로그래머스, 연습문제


def solution(k, score):
    prize = []
    answer = []

    for s in score:
        prize.append(s)
        prize.sort(reverse=True)
        if len(prize) > k:
            prize = prize[:k]

        answer.append(min(prize))

    return answer