def solution(citations):
    
    n = len(citations)
    
    for i in range(1,n+1):
        h = 0
        for j in citations:
            if i<=j:
                # h = i번 이상인게 몇 편 이상
                h += 1
        if i >= h:
            break
    
    return h
