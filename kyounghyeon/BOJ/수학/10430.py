# 제목 : 나머지
# 분류 : 수학
# 출처 : 백준 10430

a, b, c = map(int, input().split())

print((a + b) % c)
print(((a % c) + (b % c)) % c)
print((a * b) % c)
print(((a % c) * (b % c) % c))
