import sys
si = sys.stdin.readline
n, m = map(int, si().split())
a = list(map(int, si().split()))

tmp = 0
ans = 0
R = -1
for L in range(n):
    while R + 1 < n and tmp < m:
        R += 1
        tmp += a[R]
            
    if tmp == m:
        ans += 1
            
    tmp -= a[L]

print(ans)