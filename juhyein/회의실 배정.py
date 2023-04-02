N = int(input())
cnt = 0
t = []
for _ in range(N):
    x,y = map(int, input().split())
    t.append((x,y))
    
t.sort(key = lambda x : (x[1],x[0]))
end = 0
for i in range(N):
    if i == 0:
        cnt += 1
        end = t[i][1]
    elif end <= t[i][0]:
        cnt += 1
        end = t[i][1]
print(cnt)
