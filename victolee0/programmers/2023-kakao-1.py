def solution(today, terms, privacies):
    answer = []
    y, m, d = map(int, today.split('.'))
    today = int(today.replace('.', ''))
    terms = {i.split()[0]: int(i.split()[1]) for i in terms}
    month = range(1, 13)
    
    for i, privacy in enumerate(privacies):
        date, term = privacy.split()
        ny, nm, nd = map(int, date.split('.'))
        tmp_month = nm + terms[term]
        
        if tmp_month > 12:
            date = f'{ny+(tmp_month-1)//12}' +  f'{month[(tmp_month-1)%12]:0>2}' + f'{nd:0>2}'
        else:
            date = f'{ny}' + f'{tmp_month:0>2}' + f'{nd:0>2}'

        if int(today) >= int(date):
            answer += [i+1]
        
    return answer
