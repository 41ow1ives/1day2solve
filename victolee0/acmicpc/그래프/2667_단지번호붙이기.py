import sys
sys.setrecursionlimit(25*25+5)
si = sys.stdin.readline
n = int(si())
maps = [si().strip() for _ in range(n)]

visited = [[False] * n for _ in range(n)]

def dfs(x, y):
    global cnt
    cnt += 1
    visited[x][y] = True
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for i in range(4):
        if x + dx[i] < 0 or x + dx[i] >= n or y + dy[i] < 0 or y + dy[i] >= n:
            continue
        if visited[x + dx[i]][y + dy[i]]:
            continue
        
        if maps[x + dx[i]][y + dy[i]] == '1':    
            dfs(x + dx[i], y + dy[i])
        
    return cnt

ans = []
for i in range(n):
    for j in range(n):
        if visited[i][j]:
            continue
        
        if maps[i][j] == '1':
            cnt = 0
            dfs(i, j)
            ans.append(cnt)

print(len(ans))
for i in sorted(ans):
    print(i)
