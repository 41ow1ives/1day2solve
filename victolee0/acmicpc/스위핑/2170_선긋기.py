import sys
si = sys.stdin.readline
n = int(si())
lines = []
for _ in range(n):
    x, y = map(int, si().split())
    lines.append((x, y))
    
lines = sorted(lines)

s, e = lines[0]
ans = 0
for x, y in lines[1:]:
    if x > e:
        ans += e - s
        s = x
        e = y
    else:
        e = max(e, y)
        
ans += e - s
print(ans)