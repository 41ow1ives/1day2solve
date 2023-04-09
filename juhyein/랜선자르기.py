k,n = map(int, input().split())
l = [int(input()) for _ in range(k)]

start = 1
end = sum(l)//n
result = 0
while start <= end:
    total = 0
    mid = (start + end) //2
    
    for x in l:
        total += x // mid
    if total >= n :
        result = mid
        start = mid + 1
    else:
        end = mid-1

print(result)     
