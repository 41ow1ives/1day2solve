from collections import deque
limit = list(map(int, input().split()))

def move(tmp, x, y):
    res = tmp[:]
    if tmp[x] + tmp[y] <= limit[y]:
        res[y] += res[x]
        res[x] = 0
    else: # 5 1 3 -> 3 3 3
        res[x] = res[x] - (limit[y] - res[y])
        res[y] = limit[y]
    return res

Q = deque()
visit = [[[False] * (limit[2] + 1) for _ in range(limit[1] + 1)] for _ in range(limit[0] + 1)]
Q.append([0, 0, limit[2]])
visit[0][0][limit[2]] = True
possible = [0] * (limit[2] + 1)

while Q:
    now = Q.popleft()
    if now[0] == 0:
        possible[now[2]] = True
    for x in range(3):
        for y in range(3):
            if x == y: continue
            next = move(now, x, y)
            if visit[next[0]][next[1]][next[2]]: continue
            visit[next[0]][next[1]][next[2]] = True
            Q.append(next)
        
        
for i in range(limit[2] + 1):
    if possible[i]:
        print(i, end=' ')