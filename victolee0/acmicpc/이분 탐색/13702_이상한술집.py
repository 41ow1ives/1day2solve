import sys
si = sys.stdin.readline
n, k = map(int, si().split())
lst = []
for _ in range(n):
    x = int(si())
    lst.append(x)

l, r, ans = 0, 2 ** 32, 0

def determination(limit):
    if limit == 0:
        return False
    cnt = 0
    for x in lst:
        cnt += x // limit
    return cnt >= k

while l <= r:
    mid = (l + r) // 2
    if determination(mid):
        l = mid + 1
        ans = mid
    else:
        r = mid - 1        

print(ans)