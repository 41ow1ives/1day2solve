n = int(input())
a = list(map(int, input().split()))
inc = [0]*n
dec = [0]*n

# 증가, 감소를 각각 만들고 더하고 -1

for i in range(n):
    for j in range(i):
        if a[i]>a[j] and inc[j]>inc[i]:
            inc[i] = inc[j]
    inc[i] += 1
    
    
for i in range(n-1, -1,-1):
    for j in range(n-1, i-1, -1):
        if a[j]<a[i] and dec[j]>dec[i]:
            dec[i] = dec[j]
    dec[i] += 1

dp = [inc[i]+dec[i]-1 for i in range(n)]
print(max(dp))
