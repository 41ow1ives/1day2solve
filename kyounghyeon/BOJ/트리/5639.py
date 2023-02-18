# 제목 : 이진 검색 트리
# 분류 : 트리, 재귀 / Gold 5
# 출처 : 백준 5639

import sys

sys.setrecursionlimit(10 ** 6)
preord = []
while True:
    try:
        preord.append(int(sys.stdin.readline()))
    except:
        break


def postord(start, end):
    if start > end:
        return

    mid = end + 1
    for i in range(start + 1, end + 1):
        if preord[start] < preord[i]:
            mid = i
            break

    postord(start + 1, mid - 1)
    postord(mid, end)
    print(preord[start])


postord(0, len(preord)-1)
