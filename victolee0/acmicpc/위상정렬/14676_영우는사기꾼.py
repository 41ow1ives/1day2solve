import sys
si = sys.stdin.readline
n, m, k = map(int, si().split())
con = [[] for _ in range(n + 1)]
indeg = [0] * (n + 1)
for _ in range(m):
    x, y = map(int, si().split())
    con[x].append(y)
    indeg[y] += 1

cnt = [0] * (n + 1)
possible = [0] * (n + 1)
abnormal = False
for _ in range(k):
    a, x = map(int, si().split())
    if a == 1:
        if possible[x] < indeg[x]:
            abnormal = True
        cnt[x] += 1
        if cnt[x] == 1:
            for y in con[x]:
                possible[y] += 1
    else:
        if cnt[x] == 0:
            abnormal = True
        
        cnt[x] -= 1
        if cnt[x] == 0:
            for y in con[x]:
                possible[y] -= 1
                
    if abnormal:
        break
print('Lier!' if abnormal else 'King-God-Emperor')