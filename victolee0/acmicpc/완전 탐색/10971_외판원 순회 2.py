import sys
si = sys.stdin.readline
n = int(si())

W = [list(map(int, si().split())) for _ in range(n)]
visited = [False] * n
ans = int(1e6 * 16)

def dfs(start, x, dist):
    global ans
    if sum(visited) == n:
        if W[x][start]:
            dist += W[x][start]
            if ans > dist:
                ans = dist
        return
    if dist > ans:
        return
    for i in range(n):
        if not visited[i] and W[x][i]:
            visited[i] = True
            dfs(start, i, dist + W[x][i])
            visited[i] = False

for i in range(n):
    visited[i] = True
    dfs(i, i, 0)
    visited[i] = False

print(ans)