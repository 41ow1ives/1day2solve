from itertools import combinations

def solution(number):
    comb = list(combinations(number, 3))
    answer = 0
    
    for l in comb:
        if sum(l) == 0: answer += 1
    
    return answer
