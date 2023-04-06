from collections import deque
n, k = map(int, input().split())
INF = 100005
dist = [-1 for _ in range(INF)]
Q = deque([(n, 0)])

while Q:
    x, t = Q.popleft()
    if dist[x] == -1:
        dist[x] = t
    if dist[x] > t: continue
    if dist[k] != -1 and t >= dist[k]: break
    dist[x] = t
    dx = [x, -1, 1]
    for i in range(3):
        nx = x + dx[i]
        if nx < 0 or nx >= INF: continue
        if dist[nx] < t + 1 and dist[nx] != -1 and i != 0: continue
        if dist[nx] < t and dist[nx] != -1 and i == 0: continue
        if i == 0:        
            Q.append((nx, t))
        else:
            Q.append((nx, t + 1))
        
print(dist[k])