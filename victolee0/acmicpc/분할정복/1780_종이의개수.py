import sys
sys.setrecursionlimit(3 ** 7 + 5)
si = sys.stdin.readline
n = int(si())
paper = [list(map(int, si().split())) for _ in range(n)]
ans = [0, 0, 0]
def cut(n, x, y):
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                prev = paper[x + i][y + j]
            if prev == paper[x + i][y + j]:
                continue

            dx = [0, 0, 0, n // 3, n // 3, n // 3, 2 * (n // 3), 2 * (n // 3), 2 * (n // 3)]
            dy = [0, n // 3, 2 * (n // 3), 0, n // 3, 2 * (n // 3), 0, n // 3, 2 * (n // 3)]
            for t in range(9):
                cut(n // 3, x + dx[t], y + dy[t])
            return
    if prev == -1:
        ans[0] += 1
    if prev == 0:
        ans[1] += 1
    if prev == 1:
        ans[2] += 1
        
cut(n, 0, 0)
for i in ans:
    print(i)
    