# 제목 : 뱀과 사다리 게임
# 분류 : BFS, Gold 5
# 출처 : 백준 16928

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

move = [0] * 101
for _ in range(n+m):
    a, b = map(int, sys.stdin.readline().split())
    move[a] = b

visited = [False] * 101
board = [0] * 101

def game():
    q = deque()
    q.append((1,0))
    visited[1] = True

    while q:
        current, t = q.popleft()
        t += 1

        for i in range(1, 7):
            next = current + i
            if next > 100 or visited[next]:
                continue

            visited[next] = True
            if move[next]:
                board[move[next]] = t
                visited[move[next]] = True
                q.append((move[next], t))
            else:
                board[next] = t
                q.append((next, t))

game()
print(board[100])