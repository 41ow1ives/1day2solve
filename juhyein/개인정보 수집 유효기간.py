# 파기해야 할 번호 return
import pandas as pd

def solution(today, terms, privacies):
    answer = []
    term = dict(zip([i.split()[0] for i in terms], [int(i.split()[1] )for i in terms]))
    
    today = (int(today.split('.')[0]) - 2000)*28*12 + int(today.split('.')[1]) * 28 +int(today.split('.')[2])
    
    for i, p in enumerate(privacies):
        date = p.split()[0].split('.')
        d = (int(date[0]) - 2000)*28*12 + int(date[1]) * 28 +int(date[2])
        
        if today - d >= term[p.split()[1]]*28 :
            answer.append(i + 1)
    
    return answer
