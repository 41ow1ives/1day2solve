import sys
input = sys.stdin.readline

N,e,w,s,n = map(int,input().split())


dx = [1,-1,0,0]
dy = [0,0,1,-1]
percent_data= [e,w,s,n]


graph = [[0] * (2*N+1) for _ in range(2*N+1)]

answer = 0
def dfs(x,y,percent,cnt):
    global answer
    if cnt == N:
        answer += percent
        return
    now_percent = percent
    graph[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < (2*N+1) and 0<=ny < (2*N+1):
            if graph[nx][ny] == 1:
                continue
            else:
                dfs(nx,ny,now_percent*(percent_data[i]/100),cnt+1)
                graph[nx][ny] = 0

dfs(N,N,1,0)

print(answer)
