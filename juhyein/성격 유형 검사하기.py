# 테스트 케이스 통과, 나머지 런타임 에러
def solution(survey, choices):
    answer = ""
    points = {1:3, 2:2, 3:1, 4:0, 5:1, 6:2, 7:3}
    result = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}
    
    for s, c in zip(survey, choices):
        types = ''
        if c <= 3 : types = s[0]
        elif c >= 5 : types = s[1]
        else : pass
        
        result[types] += points[c]
        
    types = list(result.keys())
    point = list(result.values())
    
    for i in range(0, 8, 2):
        if point[i] > point[i+1]:
            answer += types[i]
        elif point[i] < point[i+1]:
            answer += types[i+1]
        else :
            answer += sorted([types[i], types[i+1]])[0]
    
    return answer
