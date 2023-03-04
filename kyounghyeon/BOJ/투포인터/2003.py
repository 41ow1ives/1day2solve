# 제목 : 수들의 합 2
# 분류 : 투포인터 , Silver 4
# 출처 : 백준 2003

n, m = map(int, input().split())
A = list(map(int, input().split()))

e = 0
current_sum = 0
cnt = 0

for s in range(n):

    while current_sum < m and e < n:
        current_sum += A[e]
        e += 1

    if current_sum == m:
        cnt += 1

    current_sum -= A[s]

print(cnt)