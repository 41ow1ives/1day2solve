from collections import defaultdict

def date_to_day(date:str) -> int:
    year, month, date = date.split('.')
    year = int(year) * 12 * 28
    month = int(month) * 28
    day = year + month + int(date)
    return day

def solution(today:str, terms:list, privacies:list) -> list:
    answer = []
    terms = {term.split()[0]:int(term.split()[1])*28 for term in terms} # terms를 dict 형태로 바꿈 (w. month to day)
    today = date_to_day(today)
    for idx, privacy in enumerate(privacies, 1):
        date, term = privacy.split(' ')
        day = date_to_day(date)
        if day + terms[term] <= today: # 정보를 얻은 날짜에 term date를 더한 값이 오늘 보다 같거나 작으면 보존
            answer.append(idx)
    return answer


"""
# 첫번째 풀이
def calc_final_date(privacy_and_term, rule_terms):
    privacy, term = privacy_and_term.split(' ')
    # privacy에서 하루를 빼 주는 함수
    year, month, date = map(int, privacy.split('.'))
    date -= 1
    if date == 0: # date에서 하루 뺐을 때 0이면 지난 달로 넘어가야함
        date = 28
        month -= 1  
        if month == 0: # 지난 달로 넘어갔을 때 0이면 지난 해로 넘어가야함
            month = 12
            year -= 1
    # term에 따라 개월 수를 더해줄 것
    month += rule_terms[term]
    while month > 12: # month의 범위가 1부터 28이므로 while문으로 접근
        month -= 12
        year += 1
    if month < 10:
        month = f"0{month}"
    if date < 10:
        date = f"0{date}"
    return year, month, date

def solution(today, terms, privacies):
    answer = []
    # terms를 dict로 만들어서 privacies에서 꺼내오기 쉽게 만듦
    rule_terms = { term.split()[0]: int(term.split()[1]) for term in terms }
    for idx, privacy_and_term in enumerate(privacies):
        year, month, date = calc_final_date(privacy_and_term, rule_terms)
        # year month date와 today를 비교
        check_date = f"{year}.{month}.{date}"
        if today > check_date: # 텍스트로 대소 비교 바로 가능
            answer.append(idx+1)
    return answer
"""