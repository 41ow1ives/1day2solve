import sys
si = sys.stdin.readline
n, m = map(int, si().split())
a = []
for _ in range(n):
    a.append(int(si()))
    
a.sort()
R, ans = 0, a[n - 1] - a[0]
for L in range(n):
    while R + 1 < n and a[R] - a[L] < m:
        R += 1

    if a[R] - a[L] >= m:
        ans = min(a[R] - a[L], ans)
print(ans)