# 2023 카카오 블라인드 채용 Lv2
# 완전탐색

def solution(users, emoticons):
    global dc_combinations

    dc = [10, 20, 30, 40]
    seq = []
    dc_combinations = []

    '''모든 할인율 조합 구하기 (중복순열)'''
    def _H():

        if len(seq) == len(emoticons):
            dc_combinations.append(seq[:])
            return

        for d in dc:
            seq.append(d)
            _H()
            seq.pop()

    _H()

    '''모든 할인율 조합에 대해 완전탐색'''
    result_lst = []
    for dc_rates in dc_combinations:

        join = 0  # 할인율 조합별 임티 플러스 가입자 수
        amt = 0  # 할인율 조합별 총 매출액

        for u in users:

            user_buy_amt = 0  # 유저별 구입 금액
            min_rate, min_amt = u[0], u[1]

            for i, d in enumerate(dc_rates):
                if d >= min_rate:
                    user_buy_amt += emoticons[i] * (1 - (d / 100))

                if i + 1 == len(emoticons):  # 마지막에만 구입 금액 비교해서 가입자 수 / 매출액 계산
                    if user_buy_amt >= min_amt:  # 넘으면 가입자 +
                        join += 1
                    else:  # 안 넘으면 매출액 +
                        amt += user_buy_amt

        result_lst.append([join, amt])

    answer = max(result_lst)

    return answer