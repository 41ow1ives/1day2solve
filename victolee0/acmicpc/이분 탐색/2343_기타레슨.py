n, m = map(int, input().split())
lengths = list(map(int, input().split()))

def determination(limit):
    cnt = 0
    tmp = 0
    for length in lengths:
        tmp += length
        if tmp > limit:
            cnt += 1
            tmp = length
    if tmp > 0:
        cnt += 1        
    
    if cnt > m:
        return False
        
    return True

low = max(lengths)
high = 10000 * n
ans = 0
while low <= high:
    mid = (low + high) // 2
    if determination(mid):
        ans = mid
        high = mid - 1
    else:
        low = mid + 1

print(ans)