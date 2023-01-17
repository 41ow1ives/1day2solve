# 제목 : 색종이 만들기
# 분류 : 분할정복/재귀, Silver 2
# 출처 : 백준 2630

import sys

n = int(input())
paper = [[] for _ in range(n)]
for i in range(n):
    paper[i] = list(map(int, sys.stdin.readline().split()))

blue, white = 0, 0

# x, y 좌상단 좌표
# n 사각형의 한 변의 길이
def blue_white(x, y, n):
    global blue, white
    color = paper[x][y] # 좌상단 색 입력
    for i in range(x, x+n): # 탐색할 가로 범위
        for j in range(y, y+n): # 탐색할 세로 범위
            if color != paper[i][j]:
                '''
                맨 첫 색깔이 현재 탐색 중인 색과 다르다면
                4분할 해서 재탐색
                '''
                blue_white(x, y, n // 2)
                blue_white(x, y + n // 2, n // 2)
                blue_white(x + n // 2, y, n // 2)
                blue_white(x + n // 2, y + n // 2, n // 2)
                return

    if color == 0:
        white += 1
    else:
        blue += 1

blue_white(0,0,n)
print(white)
print(blue)
