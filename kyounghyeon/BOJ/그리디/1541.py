# 제목 : 잃어버린 괄호
# 분류 : 그리디, Silver 2
# 출처 : 백준 1541

form = input().split('-')
first = sum(list(map(int, form[0].split('+'))))

for i in form[1:]:
    num = list(map(int, i.split('+')))
    first -= sum(num)

print(first)