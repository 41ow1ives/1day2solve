import sys
si = sys.stdin.readline
r, c = map(int, si().split())
boards = []
for _ in range(r):
    alphabet = si().strip()
    boards += [alphabet]
    
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

cnt = 1
path = boards[0][0]
answer = 1

def rec_func(x, y):
    global cnt
    global path
    global answer
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            continue
        if boards[nx][ny] in path:
            continue
        path += boards[nx][ny]
        cnt += 1
        answer = max(cnt, answer)
        rec_func(nx, ny)
        cnt -= 1
        path = path[:cnt]
        
rec_func(0, 0)
print(answer)