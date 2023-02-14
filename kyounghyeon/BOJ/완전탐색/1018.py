# 제목 : 체스판 다시 칠하기
# 분류 : 브루트포스 / Silver 4
# 출처 : 백준 1018


n, m = map(int, input().split())
board = []

for _ in range(n):
    board.append(input())

cnt_lst = []
for row in range(n-7):
    for col in range(m-7):
        W_cnt = 0 # 시작지점 (row, col)이 W로 시작할 경우 칠하는 수
        B_cnt = 0 # 시작지점 (row, col)이 B로 시작할 경우 칠하는 수

        for i in range(8):
            for j in range(8):
                if (i+j) % 2 == 0:
                    if board[row+i][col+j] != 'W':
                        W_cnt += 1
                    elif board[row+i][col+j] != 'B':
                        B_cnt += 1
                else:
                    if board[row+i][col+j] != 'W':
                        B_cnt += 1
                    elif board[row+i][col+j] != 'B':
                        W_cnt += 1

        cnt_lst.append(min(W_cnt, B_cnt))

print(min(cnt_lst))