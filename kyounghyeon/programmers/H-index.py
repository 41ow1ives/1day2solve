# 제목 : H-index
# 분류 : 정렬, Lv 2
# 출처 : 프로그래머스

def solution(citations):
    citations.sort()
    n = len(citations)

    for i, p in enumerate(citations):
        if p >= n - i:
            return n - i

    return 0