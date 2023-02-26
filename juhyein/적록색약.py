N = int(input())
graph_n = []
graph_a = []

for _ in range(N):
    colors = input()
    graph_n.append(list(colors))
    graph_a.append(list(colors.replace("R","G")))
    
    
dx = [-1,1,0,0]
dy = [0,0,1,-1]

from collections import deque

def bfs(x,y,graph):
    q = deque([(x,y)])
    c = graph[x][y]
    # 방문처리
    graph[x][y] = 0
  
  #q 사라질 때까지 bfs다 하면 count +1
  
    while q:
        a,b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if min(nx, ny) <0 or max(nx,ny) >= N or graph[nx][ny] != c:
                pass
            else:
                q.append((nx,ny))
                graph[nx][ny] = 0
        
counts = [0,0]

for i in range(N):
    for j in range(N):
        if graph_n[i][j] != 0:
            counts[0] += 1
            bfs(i,j,graph_n)
     
for i in range(N):
    for j in range(N):
        if graph_a[i][j] != 0:
            counts[1] += 1
            bfs(i,j,graph_a)
            
            
print(counts[0],counts[1])            
