# 제목 : 피보나치 함수
# 분류 : DP, Silver 3
# 출처 : 백준 1003


t = int(input())
n_lst = [int(input()) for _ in range(t)]
fib_lst = [(0,0)] * (max(n_lst)+1)
fib_lst[0] = (1,0)
if max(n_lst) > 0:
    fib_lst[1] = (0,1)

if max(n_lst) > 2:
    for i in range(2, len(fib_lst)):
        fib_lst[i] = (fib_lst[i-1][0] + fib_lst[i-2][0], fib_lst[i-1][1] + fib_lst[i-2][1])

for n in n_lst:
    print(fib_lst[n][0], fib_lst[n][1])