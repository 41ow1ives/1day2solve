import sys
si = sys.stdin.readline
n, m = map(int, si().split())
a = []
for _ in range(n):
    x = int(si())
    a.append(x)
    
low = max(a)
high = 1000000000
ans = 0
while low <= high:
    mid = (low + high) // 2
    tmp = 0
    cnt = 1
    for x in a:
        if x + tmp > mid:
            tmp = x
            cnt += 1
        else:
            tmp += x
            
    if cnt > m:
        low = mid + 1
    else:
        ans = mid
        high = mid - 1
print(ans)
