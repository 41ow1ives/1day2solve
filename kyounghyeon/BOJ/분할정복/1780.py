# 제목 : 종이의 개수
# 분류 : 분할정복/재귀, Silver 2
# 출처 : 백준 1780

import sys

input = sys.stdin.readline
n = int(input())
paper = []
for _ in range(n):
    paper.append(list(map(int, input().split())))

m_one = 0
zero = 0
one = 0

def find(x, y, n):
    global m_one, zero, one
    num = paper[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):

            if num != paper[i][j]:

                find(x, y, n // 3)
                find(x + n // 3, y, n // 3)
                find(x + 2*(n // 3), y, n // 3)
                find(x, y + n // 3, n // 3)
                find(x, y + 2*(n // 3), n // 3)
                find(x + n // 3, y + n // 3, n // 3)
                find(x + 2*(n // 3), y + n // 3, n // 3)
                find(x + n // 3, y + 2*(n // 3), n // 3)
                find(x + 2*(n // 3), y + 2*(n // 3), n // 3)
                return

    if num == -1:
        m_one += 1
    elif num == 0:
        zero += 1
    elif num == 1:
        one += 1

find(0,0,n)

print(m_one)
print(zero)
print(one)