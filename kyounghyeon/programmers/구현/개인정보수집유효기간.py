# 제목 : 개인정보 수집 유효기간
# 분류 : 구현
# 출처 : 프로그래머스, 2023 kakao blind recruitment

def solution(today, terms, privacies):
    answer = []
    today_ymd = list(map(int, today.split(".")))
    terms = {i.split()[0]: int(i.split()[1]) for i in terms}

    for i, pri in enumerate(privacies):
        pri_ymd = list(map(int, pri[:10].split(".")))

        diff = [today_ymd[k] - pri_ymd[k] for k in range(3)]
        diff[0] = diff[0]*12*28
        diff[1] = diff[1]*28

        if terms[pri[-1]]*28 <= sum(diff):
            answer.append(i+1)

    return answer