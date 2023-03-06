# 제목 : 부분합
# 분류 : 투포인터 , Gold 3
# 출처 : 백준 1806

n, s = map(int, input().split())
A = list(map(int, input().split()))

# 연속된 수들의 부분합 중 합이 s 이상되는 것 중 가장 짧은 것의 길이
m = 100001
e = 0
current_sum = 0

for i in range(n):

    while current_sum < s and e < n:
        print(current_sum, i, e)
        current_sum += A[e]
        e += 1

    if current_sum >= s:
        m = min(m, e-i)
        print(m)

    current_sum -= A[i]

if m > 100000:
    print(0)
else:
    print(m)