import sys
si = sys.stdin.readline

n, m = map(int, si().split())
trees = list(map(int, si().split()))

def determination(x):
    ans = 0
    for i in range(n):
        ans += max(0, trees[i] - x)
   
    return ans >= m
    
L, R = 0, 2000000000
ans = 0
while L <= R:
    mid = (L + R) // 2
    if determination(mid):
        ans = max(ans, mid)
        L = mid + 1
    else:
        R = mid - 1
print(ans)