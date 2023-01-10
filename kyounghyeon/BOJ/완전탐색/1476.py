# 제목 : 날짜 계산
# 분류 : 수학, 완전탐색
# 출처 : 백준 1476

e, s, m = map(int, input().split())
year = 1

while True:
    if (year - e) % 15 == 0 and (year - s) % 28 == 0 and (year - m) % 19 == 0:
        print(year)
        break
    year += 1
