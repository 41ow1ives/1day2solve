def solution(s):
    s = list(s.lower())
    n = len(s)
    answer = ''
    ind = [i for i in range(n) if s[i] == " "]
    s[0] = s[0].upper()
    for i in ind : 
        if i == n-1 : break
        s[i+1] = s[i+1].upper()
    for i in range(n) : answer += s[i]
