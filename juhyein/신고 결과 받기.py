# 내 답안
def solution(id_list, report, k):
    answer = [0]*len(id_list)
    
    # 중복신고 제거
    r_set = list(set(report))
    
    reported_id = [i.split()[1] for i in r_set]
    report_id = [i.split()[0] for i in r_set]
    
    # 정지대상 id
    reported = []
    for id in id_list:
        if reported_id.count(id)>=k :
            reported.append(id)
    
    for i, id in enumerate(reported_id):
        if id in reported:
            x = report_id[i]
            answer[id_list.index(x)] += 1
    
    
    return answer
  
# 참고1

def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer

# 참고2

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    dic_report = {id: [] for id in id_list} # 해당 유저를 신고한 ID
    for i in set(report):
        i = i.split()
        dic_report[i[1]].append(i[0])

    for key, value in dic_report.items():
        if len(value) >= k:
            for j in value:
                answer[id_list.index(j)] += 1

    return answer
