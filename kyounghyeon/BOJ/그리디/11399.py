# 제목 : ATM
# 분류 : 그리디, Silver 4
# 출처 : 백준 11399

n = int(input())
p = list(map(int, input().split()))

p.sort()
cum = 0
for i in range(len(p)):
    cum += sum(p[:i+1])

print(cum)
