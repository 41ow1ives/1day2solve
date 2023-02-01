# 제목 : 패션왕 신혜빈
# 분류 : 자료구조/해시, Silver 3
# 출처 : 백준 9375

t = int(input())
for _ in range(t):

    n = int(input())
    clothes = {}

    for _ in range(n):
        item, key = input().split()
        if key in clothes.keys():
            clothes[key].append(item)
        else:
            clothes[key] = [item]

    cnt = 1
    for k in clothes.keys():
        cnt *= len(clothes[k])+1
    print(cnt-1)
