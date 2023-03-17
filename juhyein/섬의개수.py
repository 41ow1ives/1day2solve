from collections import deque

dx = [0,0,1,-1,1,1,-1,-1]
dy = [1,-1,0,0,1,-1,0,1]

def bfs(x,y):
    q = deque([(x,y)])
    graph[x][y] = 0
    while q:
        a,b = q.popleft()
        for nx,ny in zip(dx,dy):
            na = a + nx
            nb = b + ny
            
            # 범위에서 벗어나는지
            if min(na,nb) < 0 or na>(w-1) or nb>(h-1) or graph[na][nb] == 0 :
                pass
            else:
                q.append((na,nb))
                graph[na][nb] = 0


ans = []
while True:
    w,h = map(int, input().split())
    if w ==0 and h == 0:
        break
    cnt = 0
    graph = [ ]
    for i in range(h):
        graph.append(list(map(int, input().split())))

    for i in range(w):
        for j in range(h):
            cnt += 1
            bfs(i,j)
    ans.append(cnt)
    
for cnt in ans:
    print(cnt)
