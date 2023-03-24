from collections import Counter

def solution(k, tangerine):
    cnt = Counter(tangerine)
    tangerine.sort()
    tangerine.sort(key = lambda x : cnt[x], reverse = True)
    
    return len(set(tangerine[0:k]))
