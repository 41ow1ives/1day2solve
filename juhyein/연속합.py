N = int(input())
s = list(map(int, input().split()))
d = [0]*N

for i in range(N):
    if i == 0:
        d[i] = s[i]
    else:
        d[i] = max(d[i-1]+s[i],s[i])
        
print(max(d))        
