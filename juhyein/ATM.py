N = int(input())
p = list(map(int ,input().split()))
p.sort()

ans = 0
for i in range(N):
    ans += p[i]*(N-i)
    
print(ans)    
