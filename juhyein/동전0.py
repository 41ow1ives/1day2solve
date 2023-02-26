n,k = map(int, input().split())
coins = []
ans = 0
for _ in range(n): 
    coins.append(int(input()))
    
for c in coins[::-1]:
    if c > k : 
        pass
    ans += k//c
    k %= c
    
print(ans)
