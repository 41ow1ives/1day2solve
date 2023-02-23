# 제목 : N-Queen
# 분류 : 완전탐색/백트래킹, Gold 4
# 출처 : 백준 9663

n = int(input())
chess = [0 for _ in range(n)]
cnt = 0

def possible(row, col): # x행 i열에 퀸을 둘 경우
    for k in range(row): # x행보다 작은 행들 (이미 퀸이 있는 행에 대해)
        if col == chess[k] or (row - k == abs(col - chess[k])):
            '''
            i == chess[k] : 같은 열에 퀸이 존재
            x - k == abs(i - chess[k]) : 대각선에 퀸이 존재
            '''
            return False
    return True

def dfs(row):

    global cnt
    if row == n:
        cnt += 1
        return

    for i in range(n):
        if possible(row, i):
            chess[row] = i
            dfs(row+1)
            chess[row] = 0

dfs(0)
print(cnt)