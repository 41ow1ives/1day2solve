import sys
si = sys.stdin.readline
n = int(si())
m = int(si())
lst = list(map(int, si().split()))

l, r, ans = 0, 100000, 0
lst.sort()

def determination(limit):
    last = 0
    for x in lst:
        if x - limit <= last:
            last = x + limit
        else:
            return False
    return last >= n
            
while l <= r:
    mid = (l + r) // 2
    if determination(mid):
        ans = mid
        r = mid - 1
    else:
        l = mid + 1
print(ans)