# 제목 : 영화감독 숌
# 분류 : 완전탐색, Silver 5
# 출처 : 백준 1436

n = int(input())
k = 666
cnt = 0
while True:
    if '666' in str(k):
        cnt += 1
    if cnt == n:
        print(k)
        break
    k += 1




