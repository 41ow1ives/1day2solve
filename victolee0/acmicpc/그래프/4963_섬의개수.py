import sys
sys.setrecursionlimit(100005)
si = sys.stdin.readline

dx = [0, 0, 1, -1, 1, -1, 1, -1]
dy = [-1, 1, 0, 0, 1, 1, -1, -1]

def dfs(x, y):
    for i in range(8):
        if 0 <= x + dx[i] < h and 0 <= y + dy[i] < w:
            if maps[x + dx[i]][y + dy[i]]:
                maps[x + dx[i]][y + dy[i]] = 0
                dfs(x + dx[i], y + dy[i])

while True:
    w, h = map(int, si().split())
    if w == 0 and h == 0:
        break
    maps = []
    for _ in range(h):
        maps.append(list(map(int, si().split())))
    ans = 0
    for x in range(h):
        for y in range(w):
            if maps[x][y]:
                dfs(x, y)
                ans += 1
    print(ans)