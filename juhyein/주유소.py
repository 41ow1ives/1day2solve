N = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))[0:N-1]

c = cost[0]
for i in range(N-1):
    c = min(c, cost[i])
    cost[i] = c
    
ans = sum([cost[i]*dist[i] for i in range(N-1)])
print(ans)
