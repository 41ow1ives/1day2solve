import sys
si = sys.stdin.readline
n, k = map(int, si().split())
dolls = list(map(int, si().split()))

R, ans, tmp = -1, 10 ** 7, 0
for L in range(n):
    while R + 1 < n and tmp < k:
        R += 1
        if dolls[R] == 1:
            tmp += 1
            
    if tmp >= k:
        ans = min(ans, R - L + 1)
        
    if dolls[L] == 1:
        tmp -= 1
        
if ans == 10 ** 7:
    print(-1)
else:
    print(ans)
