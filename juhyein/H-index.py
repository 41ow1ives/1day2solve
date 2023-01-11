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


#참고1

def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer


#참고2
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0
